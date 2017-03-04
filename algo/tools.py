#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from enum import Enum, unique


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
    # 0 - our user, 1 - his partner
    def __init__(self, type: CategoryType, data_0, data_1):
        self.type = type
        self.data_0 = data_0
        self.data_1 = data_1


@unique
class UpdateType(Enum):
    INCOME_MSG = 1
    OUTCOME_MSG = 2
    OUTCOME_TIP_MSG = 3
    DELETE_TIP = 4


class UpdateInfo:
    
    TAG = 'UpdateInfo'

    def __init__(self, type: UpdateType, msg: str = None, tip_id: int = None):
        self.type = type
        if self.type is UpdateType.INCOME_MSG:
            if msg is None:
                raise ValueError('{}: message should not be empty'.format(self.TAG))
            self.msg = msg
        elif self.type is UpdateType.OUTCOME_MSG:
            if msg is None:
                raise ValueError('{}: message should not be empty'.format(self.TAG))
            self.msg = msg
        elif self.type is UpdateType.OUTCOME_TIP_MSG:
            if msg is None:
                raise ValueError('{}: message should not be empty'.format(self.TAG))
            if tip_id is None:
                raise ValueError('{}: tip id should not be empty'.format(self.TAG))
            self.msg = msg
            self.tip_id = tip_id
        elif self.type is UpdateType.DELETE_TIP:
            if tip_id is None:
                raise ValueError('{}: tip id should not be empty'.format(self.TAG))
            self.tip_id = tip_id


class DataNLP:

    def __init__(self):
        # TODO: place for smth interesting :)
        pass
