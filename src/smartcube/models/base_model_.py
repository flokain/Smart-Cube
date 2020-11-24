import ujson as json
import btree
from smartcube import util


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
    def get_by_id(cls, key):
        try:
            file = open(cls.database, "r+b")
        except OSError:
            file = open(cls.database, "w+b")
        db = btree.open(file)

        value = db[key.encode()].decode()

        db.close()
        file.close()

        return cls.from_dict(json.loads(value))

    @classmethod
    def dump(cls):
        try:
            file = open(cls.database, "r+b")
        except OSError:
            file = open(cls.database, "w+b")
        db = btree.open(file)

        with open("/database/dump.json", "w") as dump:
            dump.write("{")
            for key in db:
                dump.write(key.decode())
                dump.write(":")
                dump.write(db[key].decode())
                dump.write(",")
            dump.write("}")

        db.close()
        file.close()
