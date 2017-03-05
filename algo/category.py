#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from typing import Tuple, Dict
import logging

from .general_info import GeneralInfo
from .friends_processor import FriendsProcessor
from .music_processor import MusicProccessor
from .movie_processor import MovieProccessor
from .book_processor import BookProccessor
from .tools import UpdateInfo, InputData, DataNLP, CategoryType

module_logger = logging.getLogger('Category')


class Category: 

    TAG = 'Category'

    def __init__(self, data: Tuple[InputData]):
        self.type = data.type
        module_logger.info('Receive {} category'.format(self.type.name))
        if self.type is CategoryType.GENERAL_INFO:
            self.processor = GeneralInfo((data.data_0, data.data_1))
        elif self.type is CategoryType.MUSIC:
            self.processor = MusicProccessor( data.data_0, data.data_1 )
        elif self.type is CategoryType.BOOKS:
            self.processor = BookProccessor( data.data_0, data.data_1 )
        elif self.type is CategoryType.MOVIES:
            self.processor = MovieProccessor( data.data_0, data.data_1 )
            pass
        elif self.type is CategoryType.TRIPS:
            # TODO
            pass
        elif self.type is CategoryType.GROUPS:
            # TODO
            pass
        elif self.type is CategoryType.HASHTAGS:
            # TODO
            pass
        elif self.type is CategoryType.FRIENDS:
            self.processor = FriendsProcessor(data.data_0)
        elif self.type is CategoryType.SPORT:
            # TODO
            pass
        else:
            raise(ValueError('{}: Unsupported category type'.format(self.TAG)))
        self.intersections = self.processor.process()
        self.weight = 1

    def update(self, data: UpdateInfo, dataNLP: DataNLP):
        print( '{}: intersections count before update for {} is {}'.format(self.TAG, self.type.name, len(self.intersections)) )
        self.processor.update(data, dataNLP)
        if self.type is not CategoryType.GENERAL_INFO and self.type is not CategoryType.FRIENDS:
            self.intersections = self.processor.process()
        print( '{}: intersections count after update for {} is {}'.format(self.TAG, self.type.name, len(self.intersections)) )

    def serialize(self) -> Dict:
        output_dict = dict()
        output_dict['category_type'] = self.type.name
        output_dict['weight'] = self.weight
        output_dict['intersections'] = []
        for intersection in self.intersections:
            output_dict['intersections'].append(intersection.serialize())
        return output_dict
