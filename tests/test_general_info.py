#####
# Author: Maria Sandrikova
# Copyright 2017
#####

import unittest
import os
import json

from algo.general_info import GeneralInfo
from algo import ChatRoom, CategoryType, InputData

WORKING_DIR = os.path.dirname(__file__)
TEST_DIR = os.path.join(WORKING_DIR, 'data')
TEST_JSON = os.path.join(TEST_DIR, 'general_info.json')

class GeneralInfoTestSuite(unittest.TestCase):
    """ Tests for GeneralInfo class """

    def setUp(self):
        with open(TEST_JSON, encoding='utf8') as f:
            self.data = json.load(f)
        self.input_data = (dict(), dict())
        for i in range(2):
            for name, member in CategoryType.__members__.items():
                self.input_data[i][member] = InputData(type, None)

    def test_set_up(self):
        self.chat_room = ChatRoom(self.input_data)
        
    def test_general_info(self):
        self.input_data[0][CategoryType.GENERAL_INFO] = InputData(
            CategoryType.GENERAL_INFO, 
            self.data
        )
        self.input_data[1][CategoryType.GENERAL_INFO] = InputData(
            CategoryType.GENERAL_INFO, 
            self.data
        )
        self.chat_room = ChatRoom(self.input_data)