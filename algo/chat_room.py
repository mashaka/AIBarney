#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from typing import List, Dict, Tuple
import os
import numpy as np

from .category import Category, CategoryType, InputData
        

class ChatRoom:

    TAG = 'ChatRoom'

    def __init__(self, data: Tuple[Dict[CategoryType, InputData]]):
        self.categories = dict()
        for name, member in CategoryType.__members__.items():
            for i in range(2):
                if member not in data[i]:
                    raise ValueError('{}: Input data does not have {} type for {} user'.format(TAG, name, i+1))
            self.categories[member] = Category((data[0][member], data[1][member]))
        # TODO: calculate categories weights
        pass

    def process(self):
        pass

    def get_tips(self) -> Dict[CategoryType, Category]:
        return self.categories

   
