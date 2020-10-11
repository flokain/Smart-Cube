# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.system_config import SystemConfig  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSystemController(BaseTestCase):
    """SystemController integration test stubs"""

    def test_system_config_get(self):
        """Test case for system_config_get

        get the configuration
        """
        response = self.client.open(
            '/System/config',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_config_post(self):
        """Test case for system_config_post

        set the configuration
        """
        response = self.client.open(
            '/System/config',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_system_reboot_post(self):
        """Test case for system_reboot_post

        reboots the System
        """
        response = self.client.open(
            '/System/reboot',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
