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
MUSIC_JSON = os.path.join(TEST_DIR, 'music_info.json')
MUSIC_OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'music_info_output.json')
MOVIES_JSON = os.path.join(TEST_DIR, 'movies_info.json')
MOVIES_OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'movies_info_output.json')
BOOKS_JSON = os.path.join(TEST_DIR, 'books_info.json')
BOOKS_OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'books_info_output.json')

class GeneralInfoTestSuite(unittest.TestCase):
    """ Tests for GeneralInfo class """

    def setUp(self):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        with open(TEST_JSON, encoding='utf8') as f:
            self.data = json.load(f)
        with open(MUSIC_JSON, encoding='utf8') as f:
            self.music_data = json.load(f)
        with open(MOVIES_JSON, encoding='utf8') as f:
            self.movies_data = json.load(f)
        with open(BOOKS_JSON, encoding='utf8') as f:
            self.books_data = json.load(f)
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
            json.dump(output_dict, f, indent=4, ensure_ascii=False)

    def test_music(self):
        self.input_data.append(InputData(
            CategoryType.MUSIC, 
            self.music_data,
            self.music_data
        ))
        chat_room = ChatRoom(self.input_data)
        output_dict =  chat_room.get_tips()
        with open(MUSIC_OUTPUT_FILE, mode='w', encoding='utf8') as f:
            json.dump(output_dict, f, indent=4, ensure_ascii=False)

    def test_movies(self):
        self.input_data.append(InputData(
            CategoryType.MOVIES, 
            self.movies_data,
            self.movies_data
        ))
        chat_room = ChatRoom(self.input_data)
        output_dict =  chat_room.get_tips()
        with open(MOVIES_OUTPUT_FILE, mode='w', encoding='utf8') as f:
            json.dump(output_dict, f, indent=4, ensure_ascii=False)

    def test_books(self):
        self.input_data.append(InputData(
            CategoryType.BOOKS, 
            self.books_data,
            self.books_data
        ))
        chat_room = ChatRoom(self.input_data)
        output_dict =  chat_room.get_tips()
        with open(BOOKS_OUTPUT_FILE, mode='w', encoding='utf8') as f:
            json.dump(output_dict, f, indent=4, ensure_ascii=False)