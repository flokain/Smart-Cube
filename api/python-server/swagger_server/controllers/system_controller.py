import connexion
import six

from swagger_server.models.system_config import SystemConfig  # noqa: E501
from swagger_server.models.wifi import Wifi  # noqa: E501
from swagger_server import util


def system_config_wifi_get():  # noqa: E501
    """get configured wifi(s)

    returns wifi # noqa: E501


    :rtype: Wifi
    """
    return 'do some magic!'


def system_config_wifi_post(body=None):  # noqa: E501
    """return configured wifi

    returns current configuration if accepted # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Wifi
    """
    if connexion.request.is_json:
        body = Wifi.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def system_reboot_post():  # noqa: E501
    """reboots the System

    returns current configuration if accepted # noqa: E501


    :rtype: SystemConfig
    """
    return 'do some magic!'
