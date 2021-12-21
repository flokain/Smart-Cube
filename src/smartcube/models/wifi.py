from smartcube.models.base_model import Model
from smartcube import util


class Wifi(Model):

    def __init__(self, id: StopIteration = None, ssid: str = None, password: str = None, prefered_ip_address: str = None):
        """Wifi - a model defined in Swagger

        :param id: The id of this Wifi.
        :type id: Id
        :param ssid: The ssid of this Wifi.
        :type ssid: str
        :param password: The password of this Wifi.
        :type password: Password
        :param prefered_ip_address: The prefered_ip_address of this Wifi.
        :type prefered_ip_address: Ip
        """
        self.swagger_types = {
            'id': str,
            'ssid': str,
            'password': str,
            'prefered_ip_address': str
        }

        self.attribute_map = {
            'id': 'id',
            'ssid': 'ssid',
            'password': 'password',
            'prefered_ip_address': 'prefered-ip-address'
        }
        self._id = id
        self._ssid = ssid
        self._password = password
        self._prefered_ip_address = prefered_ip_address

    @classmethod
    def from_dict(cls, dikt) -> 'Wifi':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Wifi of this Wifi.
        :rtype: Wifi
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Wifi.


        :return: The id of this Wifi.
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Wifi.


        :param id: The id of this Wifi.
        :type id: Id
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def ssid(self) -> str:
        """Gets the ssid of this Wifi.

        the SSID of the Wifi to connect to

        :return: The ssid of this Wifi.
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid: str):
        """Sets the ssid of this Wifi.

        the SSID of the Wifi to connect to

        :param ssid: The ssid of this Wifi.
        :type ssid: str
        """
        if ssid is None:
            raise ValueError("Invalid value for `ssid`, must not be `None`")

        self._ssid = ssid

    @property
    def password(self) -> str:
        """Gets the password of this Wifi.


        :return: The password of this Wifi.
        :rtype: Password
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this Wifi.


        :param password: The password of this Wifi.
        :type password: Password
        """

        self._password = password

    @property
    def prefered_ip_address(self) -> str:
        """Gets the prefered_ip_address of this Wifi.


        :return: The prefered_ip_address of this Wifi.
        :rtype: Ip
        """
        return self._prefered_ip_address

    @prefered_ip_address.setter
    def prefered_ip_address(self, prefered_ip_address: str):
        """Sets the prefered_ip_address of this Wifi.


        :param prefered_ip_address: The prefered_ip_address of this Wifi.
        :type prefered_ip_address: Ip
        """

        self._prefered_ip_address = prefered_ip_address
