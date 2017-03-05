#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from typing import List, Tuple
import json
import logging

from .intersection import Intersection
from .tip import Tip
from .tools import UpdateInfo, DataNLP, UpdateType

module_logger = logging.getLogger('GeneralInfo')

NOT_FOUND = -1

ID = 'id'
NAME = 'name'

EDUCATION = 'education'
SCHOOL = 'school'

WORK = 'work'
EMPLOYER = 'employer'
POSITION = 'position'

HOMETOWN = 'hometown'

class GeneralInfo:

    def __init__(self, data: Tuple):
        self.data = data

    def process(self) -> List[Intersection]:
        self.intersections = []
        # Education intersections
        self.find_education_intersection()
        # Work experience intersection
        self.find_experience_intersection()
        # Home hometown intersetion
        self.find_hometown_intersection()
        module_logger.info('Find {} intersections'.format(len(self.intersections)))
        return self.intersections

    def find_education_intersection(self):
        if EDUCATION not in self.data[0] or EDUCATION not in self.data[1]:
            module_logger.info('Receive no info about education')
            return
        for education_0 in self.data[0][EDUCATION]:
            for education_1 in self.data[1][EDUCATION]:
                if education_0[SCHOOL][ID] == education_1[SCHOOL][ID]:
                    self.intersections.append(
                        self.get_education_intersection((
                            education_0,
                            education_1
                    )))

    def get_education_intersection(self, educations: Tuple) -> Intersection:
        desc = 'You both studied in {}'.format(educations[0][SCHOOL][NAME])
        weight = 1
        content = (None, None)
        tips = [
            Tip(
                'Wow, i have just seen in your facebook that we both studied in {}. That\'s cool!'.format(
                    educations[0][SCHOOL][NAME]
                ),
                1
            ),
            Tip(
                'Do you love {}? I also studied there and these days were great :)'.format(
                    educations[0][SCHOOL][NAME]
                ),
                1
            )
        ]
        return Intersection(desc, weight, content, tips)

    def find_experience_intersection(self):
        if WORK not in self.data[0] or WORK not in self.data[1]:
            module_logger.info('Receive no info about work experience')
            return
        for work_0 in self.data[0][WORK]:
            for work_1 in self.data[1][WORK]:
                if work_0[EMPLOYER][ID] == work_1[EMPLOYER][ID]:
                    self.intersections.append(
                        self.get_employer_intersection((
                            work_0,
                            work_1
                    )))
                if work_0[POSITION][ID] == work_1[POSITION][ID]:
                    self.intersections.append(
                        self.get_position_intersection((
                            work_0,
                            work_1
                    )))

    def get_employer_intersection(self, works: Tuple) -> Intersection:
        desc = 'You both workes in {}'.format(works[0][EMPLOYER][NAME])
        weight = 1
        content = (None, None)
        tips = [
            Tip(
                'Wow, i have just seen in your facebook that we both work in {}. That\'s cool!'.format(
                    works[0][EMPLOYER][NAME]
                ),
                1
            ),
            Tip(
                'Do you love {}? I also worked there and these days were great :)'.format(
                    works[0][EMPLOYER][NAME]
                ),
                1
            )
        ]
        return Intersection(desc, weight, content, tips)

    def get_position_intersection(self, works: Tuple) -> Intersection:
        desc = 'You both workes as {}'.format(works[0][POSITION][NAME])
        weight = 0.9
        content = (None, None)
        tips = [
            Tip(
                'Wow, you are also {}. That\'s cool!'.format(
                    works[0][POSITION][NAME]
                ),
                1
            )
        ]
        return Intersection(desc, weight, content, tips)

    def find_hometown_intersection(self):
        if HOMETOWN not in self.data[0] or HOMETOWN not in self.data[1]:
            module_logger.info('Receive no info about hometown')
            return
        if self.data[0][HOMETOWN][ID] == self.data[1][HOMETOWN][ID]:
            self.intersections.append(
                self.get_hometown_intersection(
                    self.data[0][HOMETOWN][NAME]
            ))

    def get_hometown_intersection(self, hometown: str) -> Intersection:
        desc = 'You both born in {}'.format(hometown)
        weight = 1
        content = (None, None)
        tips = [
            Tip(
                'You also from {}, aren\'t you?'.format(
                    hometown
                ),
                1
            )
        ]
        return Intersection(desc, weight, content, tips)

    def update(self, data: UpdateInfo, dataNLP: DataNLP):
        if UpdateType.DELETE_TIP == data.type:
            self.filter_tip(data.tip_id)

    def filter_tip(self, tip_id: int):
        for j, intersection in enumerate(self.intersections):
            for i, tip in enumerate(intersection.tips):
                if tip.id == tip_id:
                    del intersection.tips[i]
                    break
            if len(intersection.tips) == 0:
                del self.intersections[j]
                break


            
