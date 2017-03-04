#####
# Author: Maria Sandrikova
# Copyright 2017
#####

import unittest
import os

WORKING_DIR = os.path.dirname(__file__)

from algo import ChatRoom, CategoryType, InputData

class ChatRoomTestSuite(unittest.TestCase):
    """ Tests for ChatRoom class """

    def setUp(self):
        self.input_data = (dict(), dict())
        for i in range(2):
            for name, member in CategoryType.__members__.items():
                self.input_data[i][member] = InputData(type, None)

    def test_set_up(self):
        self.chat_room = ChatRoom(self.input_data)
    