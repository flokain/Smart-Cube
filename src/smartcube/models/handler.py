import logging
from urequests import request
import ujson as json

from smartcube import util
from smartcube.models.base_model import Model, database_operation
from smartcube.models.http_request import HttpRequest
from smartcube.models.event_id import EventId

log = logging.getLogger(__name__)


class Handler(Model):

    def __init__(self, id: str = None, event_id: str = None, request: HttpRequest = None, expected_response_code: int = None):  # noqa: E501
        """Handler - a model defined in Swagger

        :param id: The id of this Handler.  # noqa: E501
        :type id: str
        :param event_id: The event_id of this Handler.  # noqa: E501
        :type event_id: EventId
        :param request: The request of this Handler.  # noqa: E501
        :type request: HttpRequest
        :param expected_response_code: The expected_response_code of this Handler.  # noqa: E501
        :type expected_response_code: int
        """
        self.swagger_types = {
            'id': str,
            'event_id': str,
            'request': HttpRequest,
            'expected_response_code': int
        }

        self.attribute_map = {
            'id': 'id',
            'event_id': 'event-id',
            'request': 'request',
            'expected_response_code': 'expected-response-code'
        }
        self._id = id
        self._event_id = event_id
        self._request = request
        self._expected_response_code = expected_response_code

    @classmethod
    def from_dict(cls, dikt) -> 'Handler':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Handler of this Handler.  # noqa: E501
        :rtype: Handler
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Handler.


        :return: The id of this Handler.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Handler.


        :param id: The id of this Handler.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def event_id(self) -> str:
        """Gets the event_id of this Handler.


        :return: The event_id of this Handler.
        :rtype: EventId
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: str):
        """Sets the event_id of this Handler.


        :param event_id: The event_id of this Handler.
        :type event_id: EventId
        """

        self._event_id = event_id

    @property
    def request(self) -> HttpRequest:
        """Gets the request of this Handler.


        :return: The request of this Handler.
        :rtype: HttpRequest
        """
        return self._request

    @request.setter
    def request(self, request: HttpRequest):
        """Sets the request of this Handler.


        :param request: The request of this Handler.
        :type request: HttpRequest
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

    @property
    def expected_response_code(self) -> int:
        """Gets the expected_response_code of this Handler.

        if not set, any http response code <400 is considered as success.  # noqa: E501

        :return: The expected_response_code of this Handler.
        :rtype: int
        """
        return self._expected_response_code

    @expected_response_code.setter
    def expected_response_code(self, expected_response_code: int):
        """Sets the expected_response_code of this Handler.

        if not set, any http response code <400 is considered as success.  # noqa: E501

        :param expected_response_code: The expected_response_code of this Handler.
        :type expected_response_code: int
        """

        self._expected_response_code = expected_response_code

    def run(self) -> bool:
        log.info("runing http request handler: {}".format(
            self._request.__dict__))
        r = self._request
        response = request(method=r.method,
                           url=r.uri,
                           json=r.json,
                           headers=r.headers)

        try:
            if self._expected_response_code is not None:
                assert response.status_code == self._expected_response_code
            else:
                assert response.status_code < 400
            log.info(
                "Handler ran succesfully. Response was {}".format(
                    response.__dict__
                )
            )
        except AssertionError:
            log.error(
                "http request %s returned %i, but expected %i",
                r.uri,
                response.status_code,
                self._expected_response,
            )

    @classmethod
    @database_operation
    def get_all(cls, event_id=None):
        basekey = cls.__name__.encode()
        if event_id is not None and not EventId.isEvent(event_id):
            raise KeyError("unkown event-id")
        lst = []
        for k, v in cls.db.items(basekey):
            if basekey in k:
                re = cls.from_dict(json.loads(v.decode()))
                re.id = int(k.decode().split(basekey.decode())[1])

                if event_id is None or re.event_id == event_id:
                    lst.append(re)
            else:
                break
        return lst
