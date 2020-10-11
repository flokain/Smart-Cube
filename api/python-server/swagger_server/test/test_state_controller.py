# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cube_state import CubeState  # noqa: E501
from swagger_server.models.system_state import SystemState  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStateController(BaseTestCase):
    """StateController integration test stubs"""

    def test_state_side_get(self):
        """Test case for state_side_get

        get the current CubeState
        """
        response = self.client.open(
            '/state/side',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_state_system_get(self):
        """Test case for state_system_get

        get the current SystemState
        """
        response = self.client.open(
            '/state/System',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
