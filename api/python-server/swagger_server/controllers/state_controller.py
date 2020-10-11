import connexion
import six

from swagger_server.models.cube_state import CubeState  # noqa: E501
from swagger_server.models.system_state import SystemState  # noqa: E501
from swagger_server import util


def state_side_get():  # noqa: E501
    """get the current CubeState

     # noqa: E501


    :rtype: CubeState
    """
    return 'do some magic!'


def state_system_get():  # noqa: E501
    """get the current SystemState

     # noqa: E501


    :rtype: SystemState
    """
    return 'do some magic!'
