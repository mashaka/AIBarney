#####
# Author: Maria Sandrikova
# Copyright 2017
#####

id_counter = 0

class Tip:

    def __init__(self, text: str, weight: float):
        self.text = text
        self.weight = weight
        global id_counter
        id_counter += 1
        self.id = id_counter

    def serialize(self):
        output_dict = dict()
        output_dict['algo_id'] = self.id
        output_dict['weight'] = self.weight
        output_dict['text'] = self.text
        return output_dict