#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from typing import List, Dict, Tuple
import os
import numpy as np
import json
import logging

from .category import Category
from .tools import UpdateInfo, InputData, DataNLP, CategoryType, UpdateType
from .sentiment_analysis import classify

# model for sentiment analysis
sentiment_model = None

module_logger = logging.getLogger('ChatRoom')

class ChatRoom:

    TAG = 'ChatRoom'

    def __init__(self, data: List[InputData]):
        module_logger.info('Receive {} categories'.format(len(data)))
        self.categories = []
        for category_data in data:
            self.categories.append(Category(category_data))

    def update(self, data: UpdateInfo):
        is_positive = None
        if data.type is UpdateType.INCOME_MSG or \
                data.type is UpdateType.OUTCOME_MSG or \
                data.type is OUTCOME_TIP_MSG.INCOME_MSG:
            if sentiment_model is None:
                raise ValueError('{}: You should load sentiment model'.format(self.TAG))
            is_positive = classify(data.msg)
        for category in self.categories:
            category.update(data, DataNLP(is_positive))

    def get_tips(self) -> Dict[CategoryType, Category]:
        output_list = []
        for category in self.categories:
            if( len( category.intersections ) > 0 ):
                output_list.append(category.serialize())
        return output_list

