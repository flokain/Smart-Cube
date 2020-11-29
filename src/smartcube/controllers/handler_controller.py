import connexion
import six

from smartcube.models.handler import Handler
from smartcube import util


def add_side_handler(side_id, body=None):  # noqa: E501
    """configures a Handler for side {sideId}

    Adds a Handler to a side # noqa: E501

    :param side_id: 
    :type side_id: dict | bytes
    :param body: 
    :type body: dict | bytes

    :rtype: Handler
    """
    if connexion.request.is_json:
        side_id = Handler.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = Handler.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def handler_onchange_get():  # noqa: E501
    """get the current Handler for changes of CubeState

     # noqa: E501


    :rtype: Handler
    """
    return 'do some magic!123'


def handler_onchange_post(body=None):  # noqa: E501
    """configures a Handler for changes of CubeState

    Add a Handler to whenever the CubeState changes i.e. it is tilted # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Handler
    """
    if connexion.request.is_json:
        body = Handler.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def handler_side_side_id_get(side_id):  # noqa: E501
    """get the current Handler for {sideId}

     # noqa: E501

    :param side_id: 
    :type side_id: dict | bytes

    :rtype: Handler
    """
    if connexion.request.is_json:
        side_id = Handler.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic1!'
