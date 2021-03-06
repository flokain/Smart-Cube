# coding: utf-8

"""
    Smartcube API

    This APIis used to read and configure webhooks to be triggered by the sides of the cube  # noqa: E501

    OpenAPI spec version: v1
    Contact: flokain11@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.handler_api import HandlerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHandlerApi(unittest.TestCase):
    """HandlerApi unit test stubs"""

    def setUp(self):
        self.api = HandlerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_side_handler(self):
        """Test case for add_side_handler

        configures a Handler for side {sideId}  # noqa: E501
        """
        pass

    def test_handler_onchange_get(self):
        """Test case for handler_onchange_get

        get the current Handler for changes of CubeState  # noqa: E501
        """
        pass

    def test_handler_onchange_post(self):
        """Test case for handler_onchange_post

        configures a Handler for changes of CubeState  # noqa: E501
        """
        pass

    def test_handler_side_side_id_get(self):
        """Test case for handler_side_side_id_get

        get the current Handler for {sideId}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
