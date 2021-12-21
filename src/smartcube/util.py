import logging
# TODO #20: extract deserializer to be more readable on imports.

log = logging.Logger(__name__)


def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in (int, float, str, bool):
        return _deserialize_primitive(data, klass)
    elif hasattr(klass, '__origin__'):
        if klass.__origin__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__origin__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    elif klass in (list, dict, object):
        return _deserialize_object(data)
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = u"data"
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return a original value.

    :return: object.
    """
    return value


# def deserialize_date(string):
#     """Deserializes string to date.

#     :param string: str.
#     :type string: str
#     :return: date.
#     :rtype: date
#     """
#     try:
#         from dateutil.parser import parse
#         return parse(string).date()
#     except ImportError:
#         return string


# def deserialize_datetime(string):
#     """Deserializes string to datetime.

#     The string should be in iso8601 datetime format.

#     :param string: str.
#     :type string: str
#     :return: datetime.
#     :rtype: datetime
#     """
#     try:
#         from dateutil.parser import parse
#         return parse(string)
#     except ImportError:
#         return string


def deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()
    if not hasattr(instance, "swagger_types"):
        raise TypeError("klass is not serializable")

    if not isinstance(data, (list, dict)):
        raise TypeError("data needs to be list or dict")

    for attr, _attr in instance.attribute_map.items():
        if _attr in data:
            value = data[_attr]
            attr_type = instance.swagger_types[attr]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in data.items()}
