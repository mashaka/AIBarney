#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from typing import List

from .content import Content
from .tip import Tip


class Intersection:

    def __init__(self, 
            description: str, 
            weight: float, 
            content: tuple, 
            tips: List[Tip]):
        self.description = description
        self.weight = weight
        self.content = (
            Content(content[0]),
            Content(content[1])
        )
        self.tips = tips