import ujson as json
import btree
import os
from smartcube import util
import logging

log = logging.getLogger(__name__)
try:
    os.listdir("/database")
except OSError:
    os.mkdir("/database")


def database_operation(func):
    def wrapper_database_operation(*args, **kwargs):
        cls = args[0]
        try:
            file = open(cls.database, "r+b")
        except OSError:
            file = open(cls.database, "w+b")
        cls.db = btree.open(file)

        value = func(*args, **kwargs)

        cls.db.flush()
        cls.db.close()
        file.close()

        return value
    return wrapper_database_operation


class Model(object):
    # swaggerTypes: The key is attribute name and the
    # value is attribute type.
    swagger_types = {}

    # attributeMap: The key is attribute name and the
    # value is json key in definition.
    attribute_map = {}

    database = "database/smartcube_database"

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model"""
        return util.deserialize_model(dikt, cls)

    def to_dict(self):
        """Returns the model properties as a dict

        :rtype: dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model

        :rtype: str
        """
        return print(self.to_dict())

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    @classmethod
    def JSONEncodeModel(cls, obj):
        if isinstance(obj, cls):
            dikt = {}
            for attr, _ in obj.swagger_types.items():
                value = getattr(obj, attr)
                if value is None:
                    continue
                attr = obj.attribute_map[attr]
                dikt[attr] = value
            return dikt
        else:
            raise TypeError("object is not based on smartcube Model")

    @classmethod
    @database_operation
    def get_by_id(cls, key):
        k = (cls.__name__+str(key)).encode()
        value = cls.db[k].decode()
        return cls.from_dict(json.loads(value))

    @classmethod
    @database_operation
    def get_all(cls):
        basekey = cls.__name__.encode()
        lst = []
        for k, v in cls.db.items(basekey):
            if basekey in k:
                lst.append(cls.from_dict(json.loads(v.decode())))
            else:
                break
        return lst

    @classmethod
    @database_operation
    def dump(cls):
        with open("/database/dump.json", "w") as dump:
            dump.write("{")
            for key in cls.db:
                dump.write(key.decode())
                dump.write(":")
                dump.write(cls.db[key].decode())
                dump.write(",")
            dump.write("}")

    @classmethod
    @database_operation
    def _save(cls, obj, key: str = None):
        """save an object. if no id is provided the database will be scan for the next free integer for that class

        Args:
            key (str, optional): [description]. the id of the object
        """

        if key is None:
            k = 0
            while True:
                k += 1
                try:
                    cls.get_by_id(k) # if database is new this will reopen the new db and close it. the save operation will therefore fail to save data in the closed file
                    # this is a dirty hack to reopen the new database.
                except KeyError:
                    log.debug("found unused key {}".format(k))
                    key = str(k)
                    break

        k = (cls.__name__+key)
        cls.db[k.encode()] = json.dumps(cls.JSONEncodeModel(obj)).encode()
        return key

    def save(self, key=None):
        if key is not None:
            key = str(key)
        return self._save(self, key)

    @classmethod
    @database_operation
    def _delete(cls, key: str):
        del cls.db[(cls.__name__+str(key)).encode()]

    def delete(self, key=None):
        if key is not None:
            key = str(key)
        self._delete(self, str(key))
