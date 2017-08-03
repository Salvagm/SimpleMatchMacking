# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2001 import InlineResponse2001
from swagger_server.models.inline_response201 import InlineResponse201
from swagger_server.models.user import User
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMatchmakingController(BaseTestCase):
    """ MatchmakingController integration test stubs """

    def test_create_group(self):
        """
        Test case for create_group

        Add a new group to game
        """
        user = [User()]
        response = self.client.open('/matchmaking/1.0.0/matchmacking/CreateGroup',
                                    method='POST',
                                    data=json.dumps(user),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_group(self):
        """
        Test case for delete_group

        Remove group from game
        """
        user = None
        response = self.client.open('/matchmaking/1.0.0/matchmacking/leave',
                                    method='POST',
                                    data=json.dumps(user),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_group_status(self):
        """
        Test case for get_group_status

        Check if user is has party to play
        """
        query_string = [('groupId', 56)]
        response = self.client.open('/matchmaking/1.0.0/matchmacking/checkReady',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
