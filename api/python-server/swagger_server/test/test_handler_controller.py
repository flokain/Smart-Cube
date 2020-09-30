# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.handler import Handler  # noqa: E501
from swagger_server.models.side_id import SideId  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHandlerController(BaseTestCase):
    """HandlerController integration test stubs"""

    def test_add_side_handler(self):
        """Test case for add_side_handler

        configures a Handler for side {sideId}
        """
        body = Handler()
        response = self.client.open(
            '/handler/side/{sideId}'.format(side_id=SideId()),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_handler_onchange_get(self):
        """Test case for handler_onchange_get

        get the current Handler for changes of CubeState
        """
        response = self.client.open(
            '/handler/onchange',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_handler_onchange_post(self):
        """Test case for handler_onchange_post

        configures a Handler for changes of CubeState
        """
        body = Handler()
        response = self.client.open(
            '/handler/onchange',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_handler_side_side_id_get(self):
        """Test case for handler_side_side_id_get

        get the current Handler for {sideId}
        """
        response = self.client.open(
            '/handler/side/{sideId}'.format(side_id=SideId()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
