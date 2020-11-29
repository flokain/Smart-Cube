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
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(
                        x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
    def JSONEncodeModelList(cls, lst):
        if isinstance(lst, list):
            r = []
            for i in lst:
                r.append(cls.JSONEncodeModel(i))
            return r
        else:
            raise TypeError("obj is not a list of smartcube Models")

    @classmethod
    def JSONEncodeModel(cls, obj):
        if isinstance(obj, Model):
            dikt = {}
            for attr, _ in obj.swagger_types.items():
                value = getattr(obj, attr)
                if value is None:
                    continue
                attr = obj.attribute_map[attr]
                if isinstance(value, Model):
                    value = Model.JSONEncodeModel(value)
                dikt[attr] = value
            return dikt
        else:
            raise TypeError("object is not based on smartcube Model")

    @classmethod
    @database_operation
    def get_by_id(cls, key):
        k = (cls.__name__ + str(key)).encode()
        value = cls.db[k].decode()
        re = cls.from_dict(json.loads(value))
        re.id = int(key)
        return re

    @classmethod
    @database_operation
    def get_all(cls):
        basekey = cls.__name__.encode()
        lst = []
        for k, v in cls.db.items(basekey):
            if basekey in k:
                re = cls.from_dict(json.loads(v.decode()))
                re.id = int(k.decode().split(basekey)[1])
                lst.append(re)
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
    def _save(cls, obj, key=None):
        """save an object. if no id is provided the database will be scan for the next free integer for that class

        Args:
            key (str, optional): [description]. the id of the object
        """

        if key is None:
            i = 0
            while True:
                i += 1
                tmp_key = cls.__name__ + str(i)
                if tmp_key.encode() not in cls.db:
                    log.debug("found unused key {}".format(tmp_key))
                    key = i
                    break

        k = cls.__name__ + str(key)
        cls.db[k.encode()] = json.dumps(cls.JSONEncodeModel(obj)).encode()
        obj.id = int(key)
        return str(key)

    def save(self, key=None):
        return self._save(self, key)

    @classmethod
    @database_operation
    def _delete(cls, key):
        del cls.db[(cls.__name__ + str(key)).encode()]

    def delete(self, key):
        self._delete(self, key)
