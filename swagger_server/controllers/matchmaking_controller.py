import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2001 import InlineResponse2001
from swagger_server.models.inline_response201 import InlineResponse201
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from ..logic.game_controller import GroupStorageController

def create_group(user):
    """
    Add a new group to game

    :param user: Party members
    :type user: list | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        users_group = [User.from_dict(d) for d in connexion.request.get_json()]
    response = ("success", 201)
    if len(users_group) > 4:
        response = ("Max number of player is 4", 400)
    else:
        groupId = GroupStorageController.add_new_group(users_group)
    return response


def delete_group(user):
    """
    Remove group from game

    :param user: User who cancel the queue
    :type user:

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_group_status(groupId):
    """
    Check if user is has party to play

    :param groupId: Status values that need to be considered for filter
    :type groupId: int

    :rtype: InlineResponse2001
    """
    return 'do some magic!'
