import connexion
import six

from swagger_server.models.system_config import SystemConfig  # noqa: E501
from swagger_server import util


def system_config_get():  # noqa: E501
    """get the configuration

    returns current conffiguration # noqa: E501


    :rtype: SystemConfig
    """
    return 'do some magic!'


def system_config_post():  # noqa: E501
    """set the configuration

    returns current configuration if accepted # noqa: E501


    :rtype: SystemConfig
    """
    return 'do some magic!'


def system_reboot_post():  # noqa: E501
    """reboots the System

    returns current configuration if accepted # noqa: E501


    :rtype: SystemConfig
    """
    return 'do some magic!'
