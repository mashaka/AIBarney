#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from typing import Tuple
from enum import Enum, unique

from .general_info import GeneralInfo

NOT_FOUND = -1

@unique
class CategoryType(Enum):
    GENERAL_INFO = 1
    MUSIC = 2
    BOOKS = 3
    MOVIES = 4
    TRIPS = 5
    GROUPS = 6
    HASHTAGS = 7
    FRIENDS = 8
    SPORT = 9

    
class InputData:

    def __init__(self, type: CategoryType, data):
        self.type = type
        self.data = data    


class Category: 

    TAG = 'Category'

    def __init__(self, data: Tuple[InputData]):
        if data[0].type != data[1].type:
            raise ValueError('{}: input data should have equal type, but received {} and {}'.format(
                TAG,
                data[0].type.name,
                data[1].type.name
            ))
        self.type = data[0].type
        if self.type == CategoryType.GENERAL_INFO:
            # TODO
            self.intersections = GeneralInfo((data[0].data, data[1].data)).process()
        elif self.type == CategoryType.MUSIC:
            # TODO
            self.intersections = []
        elif self.type == CategoryType.BOOKS:
            # TODO
            self.intersections = []
        elif self.type == CategoryType.MOVIES:
            # TODO
            self.intersections = []
        elif self.type == CategoryType.TRIPS:
            self.intersections = []
        elif self.type == CategoryType.GROUPS:
            # TODO
            self.intersections = []
        elif self.type == CategoryType.HASHTAGS:
            # TODO
            self.intersections = []
        elif self.type == CategoryType.FRIENDS:
            # TODO
            self.intersections = []
        elif self.type == CategoryType.SPORT:
            # TODO
            self.intersections = []
        # TODO: compute intersection weights
        self.weight = NOT_FOUND

    def set_weight(self, weight: int):
        self.weight = weight