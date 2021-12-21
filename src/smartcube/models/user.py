
from smartcube.models.base_model import Model
from smartcube import util


class User(Model):

    def __init__(self, id: str = None, username: str = None, password: str = None):
        """User - a model defined in Swagger

        :param id: The id of this User.
        :type id: Id
        :param username: The username of this User.
        :type username: str
        :param password: The password of this User.
        :type password: Password
        """
        self.swagger_types = {
            'id': str,
            'username': str,
            'password': str
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'password': 'password'
        }
        self._id = id
        self._username = username
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: Id
        """

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: Password
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: Password
        """

        self._password = password
