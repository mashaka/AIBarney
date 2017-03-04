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
from .tools import UpdateInfo, InputData, DataNLP, CategoryType

module_logger = logging.getLogger('ChatRoom')

class ChatRoom:

    TAG = 'ChatRoom'

    def __init__(self, data: List[InputData]):
        module_logger.info('Receive {} categories'.format(len(data)))
        self.categories = []
        for category_data in data:
            self.categories.append(Category(category_data))
        # TODO: calculate categories weights

    def update(self, data: UpdateInfo):
        # TODO: add some NLP here
        for category in self.categories:
            category.update(data, DataNLP())

    def get_tips(self) -> Dict[CategoryType, Category]:
        output_list = []
        for category in self.categories:
            output_list.append(category.serialize())
        return output_list

