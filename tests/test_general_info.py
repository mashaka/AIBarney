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
OUTPUT_DIR = os.path.join(WORKING_DIR, 'output')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'general_info_output.json')

class GeneralInfoTestSuite(unittest.TestCase):
    """ Tests for GeneralInfo class """

    def setUp(self):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        with open(TEST_JSON, encoding='utf8') as f:
            self.data = json.load(f)
        self.input_data = []

    def test_set_up(self):
        chat_room = ChatRoom(self.input_data)
        
    def test_general_info(self):
        self.input_data.append(InputData(
            CategoryType.GENERAL_INFO, 
            self.data,
            self.data
        ))
        chat_room = ChatRoom(self.input_data)
        output_dict =  chat_room.get_tips()
        with open(OUTPUT_FILE, mode='w', encoding='utf8') as f:
            json.dump(output_dict, f, indent=4)