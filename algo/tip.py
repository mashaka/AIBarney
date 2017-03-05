#####
# Author: Maria Sandrikova
# Copyright 2017
#####


class Tip:

    id_counter = 0

    @staticmethod
    def get_next_id():
        Tip.id_counter += 1
        return Tip.id_counter

    def __init__(self, text: str, weight: float):
        self.text = text
        self.weight = weight
        self.id = self.get_next_id()

    def serialize(self):
        output_dict = dict()
        output_dict['algo_id'] = self.id
        output_dict['weight'] = self.weight
        output_dict['text'] = self.text
        return output_dict