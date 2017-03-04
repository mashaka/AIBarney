from typing import List, Dict
from .intersection import Intersection
from .tip import Tip
import random

MINIMAL_BOOKS_LIKES = 50

class BookProccessor:

    def __init__( self, firstData, secondData ):
        firstDataList = firstData["data"]
        secondDataList = secondData["data"]
        firstIds = set( map( lambda x: x["id"], firstDataList ) )
        secondIds = set( map( lambda x: x["id"], secondDataList ) )
        intersectionIds = firstIds & secondIds
        self.firstData = firstDataList
        self.secondData = secondDataList
        self.commonBooks = []

        for data in firstDataList:
            if data["id"] in intersectionIds:
                self.commonBooks.append( data )

    def process(self):

        intersections = []
        if len( self.firstData ) > MINIMAL_BOOKS_LIKES and len( self.secondData ) > MINIMAL_BOOKS_LIKES:
            intersections.append( Intersection( "Like reading books", 
            0.1, (None, None), 
            [
                Tip( "Do you actually like reading books?", 1.0 ),
                Tip( "You seem to love books. What is your favourite?", 0.9 )
            ], 
            0.1 ) )
        
        for data in self.commonBooks:
            discussBookTip = "What do you like about book " + data["name"] + "?"

            intersections.append( Intersection( "Like book " + data["name"] + "", 
                0.5, (None, None), [ Tip( discussBookTip, 0.9 ),
                Tip( discussBookTip, 1.0 ) ] ) )

        return intersections

    def update(self):
        pass
