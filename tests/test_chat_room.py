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
        self.input_data = []

    def test_set_up(self):
        self.chat_room = ChatRoom(self.input_data)
    