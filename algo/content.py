#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from enum import Enum, unique


@unique
class ContentType(Enum):
    STRING = 1,
    IMAGE_URL = 2


class Content:

    TAG = 'Content'

    def __init__(self, type: ContentType, data):
        self.data = data
        self.type = type

    def serialize(self):
        output_dict = dict()
        output_dict['type'] = self.type.name
        if ContentType.STRING is self.type or ContentType.IMAGE_URL is self.type:
            output_dict['data'] = self.data
        else:
            raise ValueError('{}: Unsupported type {} in serialization'.format(
                self.TAG, self.type.name))