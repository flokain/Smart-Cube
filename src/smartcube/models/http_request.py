from smartcube.models.base_model import Model
from smartcube import util
from ujson import loads
from urequests import request, Response


class HttpRequest(Model):
    def __init__(self, uri: str = None, method: str = "GET", headers: dict = None, payload: str = None):
        """HttpRequest - a model defined in Swagger

        :param uri: The uri of this HttpRequest.
        :type uri: str
        :param method: The method of this HttpRequest.
        :type method: str
        :param headers: The headers of this HttpRequest.
        :type headers: dict
        :param payload: The payload of this HttpRequest.
        :type payload: str
        """
        self.swagger_types = {"uri": str, "method": str, "headers": dict, "payload": str}

        self.attribute_map = {"uri": "uri", "method": "method", "headers": "headers", "payload": "payload"}
        self._uri = uri
        self._method = method
        self._headers = headers
        self._payload = payload

    @classmethod
    def from_dict(cls, dikt) -> "HttpRequest":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HttpRequest of this HttpRequest.
        :rtype: HttpRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self) -> str:
        """Gets the uri of this HttpRequest.


        :return: The uri of this HttpRequest.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        """Sets the uri of this HttpRequest.


        :param uri: The uri of this HttpRequest.
        :type uri: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")

        self._uri = uri

    @property
    def method(self) -> str:
        """Gets the method of this HttpRequest.


        :return: The method of this HttpRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method: str):
        """Sets the method of this HttpRequest.


        :param method: The method of this HttpRequest.
        :type method: str
        """
        allowed_values = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
        if method not in allowed_values:
            raise ValueError("Invalid value for `method` ({0}), must be one of {1}".format(method, allowed_values))

        self._method = method

    @property
    def headers(self) -> dict:
        """Gets the headers of this HttpRequest.


        :return: The headers of this HttpRequest.
        :rtype: dict
        """
        return self._headers

    @headers.setter
    def headers(self, headers: dict):
        """Sets the headers of this HttpRequest.


        :param headers: The headers of this HttpRequest.
        :type headers: dict
        """

        self._headers = headers

    @property
    def payload(self) -> str:
        """Gets the payload of this HttpRequest.


        :return: The payload of this HttpRequest.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload: str):
        """Sets the payload of this HttpRequest.


        :param payload: The payload of this HttpRequest.
        :type payload: str
        """

        self._payload = payload

    @property
    def json(self) -> dict:
        """Gets the payload as json dict

        Returns:
            dict: The payload of this HttpRequest as dict
        """
        return loads(self._payload)

    def execute(self) -> Response:
        return request(
            method=self.method,
            url=self.uri,
            data=self.payload,
            headers=self.headers,
        )

    # def _render(self, string, **kwargs):
    #     import ure as re
    #     for key, value in kwargs:
    #         pattern = "{{{{{}}}}}".format(key)
    #         string = re.sub(pattern, value, string)
    #     return string

    # def render(self, **kwargs):
    #     return HttpRequest(
    #         uri=self._render(self._uri, kwargs),
    #         method=self._render(self._method, kwargs),
    #         headers=[self._render(h, kwargs) for h in self._headers],
    #         payload=self._render(self._payload, kwargs)
    #     )
