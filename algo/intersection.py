#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from typing import List, Tuple

from .content import Content
from .tip import Tip


class Intersection:

    id_counter = 0

    @staticmethod
    def get_next_id():
        Intersection.id_counter += 1
        return Intersection.id_counter

    def __init__(self, 
            description: str, 
            weight: float, 
            content: Tuple[Content], 
            tips: List[Tip]):
        self.id = self.get_next_id()
        self.description = description
        self.weight = weight
        self.content = content
        self.tips = tips

    def serialize(self):
        output_dict = dict()
        output_dict['algo_id'] = self.id
        output_dict['description'] = self.description
        output_dict['weight'] = self.weight
        if self.content[0] is not None:
            output_dict['content_0'] = self.content[0].serialize()
        if self.content[1] is not None:
            output_dict['content_1'] = self.content[1].serialize()
        output_dict['tips'] = []
        for tip in self.tips:
            output_dict['tips'].append(tip.serialize())
        return output_dict
