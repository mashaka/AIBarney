from typing import List, Dict
from .intersection import Intersection
from .tip import Tip
import random

def performerTipString( data, tipBegin, tipEnd ):
    performerName = data["name"]
    
    return tipBegin + " " + performerName + " " + tipEnd

def getCoverUrl( data ):
    pictureUrl = None
    if data["cover"]:
        pictureUrl = data["cover"]["source"]
    return pictureUrl

MINIMAL_MUSIC_LIKES = 50
abusiveLoveToMusicsDefaultWeight = 0.1
suggestCommonArtistWeight = 0.5
suggestCommonGenreWeight = 0.3

class MusicProccessor:

    def __init__( firstDataList: List[Dict], secondDataList: List[Dict] ):
        firstIds = set( map( lambda x: x["id"], firstDataList ) )
        secondIds = set( map( lambda x: x["id"], secondDataList ) )
        firstGenres = set( map( lambda x: x["genre"], firstDataList) )
        secondGenres = set( map( lambda x: x["genre"], secondDataList ) ) 
        intersectionIds = firstIds & secondIds
        intersectionGenres = firstGenres & secondGenres
        self.firstData = firstDataList
        self.secondData = secondDataList
        self.commonPerformers = []

        self.genreToPerformersLists = dict()
        for genre in intersectionGenres:
            self.genreToPerformersLists["genre"] = [[], []]

        for data in firstDataList:
            if data["id"] in intersectionIds:
                self.commonPerformers.append( data )
            if data["genre"] in intersectionGenres:
                self.genreToPerformersLists[data["genre"]][0].append( data )

        for data in secondDataList:
            if data["genre"] in intersectionGenres:
                self.genreToPerformersLists[data["genre"]][1].append( data )

    def process():

        intersections = []
        if len( self.firstData ) > MINIMAL_MUSIC_LIKES and len( self.secondData ) > MINIMAL_MUSIC_LIKES:
            intersections.append( Intersection( "Abusive love to musics", 
            abusiveLoveToMusicsDefaultWeight, [None, None], 
            [
                Tip( "Do you actually like hearing musics?", 1.0 ),
                Tip( "You seem to love musics. What is your favourite?", 0.9 )
            ],
            0.1 ) )
        
        for data in self.commonPerformers:
            pictureUrl = getCoverUrl( data )
            
            confirmMutiallyLikingPerformerTip = performerTipString( data, 
                "You seem to hear music a lot. Do you actually like", "songs?")
            askAboutFavouritePerformerSongTip = performerTipString( data, 
                "You seem to like", "mucics. What is your favourite?") )

            intersections.append( Intersection( performerTipString( data, "Like music of", "" ), 
                suggestCommonArtistWeight, [pictureUrl, None], [ 
                confirmMutiallyLikingPerformerTip, askAboutFavouritePerformerSongTip ] ) )

        for genre, performersPair in self.genreToPerformersLists:
            firstList = performersPair[0]
            secondList = performersPair[1]
            firstElement = random.choice( firstList )
            secondElement = random.choice( secondList )
            firstUrl = getCoverUrl( firstElement )
            secondUrl = getCoverUrl( secondElement )

            firstName = firstElement["name"]
            secondName = secondElement["name"]

            text = "Looks like you are listening to " + genre + " music. I also do. Have you heard about " 
                + secondName + "?"

            intersections.append( Intersection( "Like music of " + genre + ": " + firstName + ", " + secondName, 
            suggestCommonGenreWeight, [ firstUrl, secondUrl ], [ Tip( text, 1.0 )  ] ) ) )

    def update():
        pass
