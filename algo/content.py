#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from enum import Enum, unique


@unique
class ContentType(Enum):
    STRING = 1


class Content:

    TAG = 'Content'

    def __init__(self, data, type: ContentType):
        self.data = data
        self.type = type

    def serialize(self):
        output_dict = dict()
        output_dict['type'] = self.type.name
        if ContentType.STRING is self.type:
            output_dict['data'] = self.data
        else:
            raise ValueError('{}: Unsupported type {} in serialization'.format(
                self.TAG, self.type.name))