# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse200(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message: str=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param message: The message of this InlineResponse200.
        :type message: str
        """
        self.swagger_types = {
            'message': str
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.
        :rtype: InlineResponse200
        """
        return deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """
        Gets the message of this InlineResponse200.

        :return: The message of this InlineResponse200.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this InlineResponse200.

        :param message: The message of this InlineResponse200.
        :type message: str
        """

        self._message = message

