from typing import List, Dict
from .intersection import Intersection
from .tip import Tip
import random
from datetime import datetime
from .content import Content, ContentType

def performerTipString(data, tipBegin, tipEnd):
    performerName = data["name"]
    return tipBegin + " " + performerName + " " + tipEnd

def getCoverUrl(data):
    pictureUrl = None
    if "cover" in data:
        pictureUrl = data["cover"]["source"]
    return pictureUrl

def findNearestEvent(data):
    if not "events" in data:
        return None
    events = data["events"]["data"]
    now = datetime.now()
    for i in range(len(events) - 1, 0, -1):
        event = events[i]
        start = datetime.strptime(event["start_time"][:-6], '%Y-%m-%dT%H:%M:%S')
        if start > now:
            return event
    return None 

MINIMAL_MUSIC_LIKES = 50
abusiveLoveToMoviesDefaultWeight = 0.1
suggestCommonArtistWeight = 0.5
suggestCommonGenreWeight = 0.3

class MusicProccessor:

    def __init__( self, firstData, secondData):
        firstDataList = firstData["data"]
        secondDataList = secondData["data"]
        firstIds = set( map( lambda x: x["id"], firstDataList ) )
        secondIds = set( map( lambda x: x["id"], secondDataList ) )
        firstGenres = set( map( lambda x: x["genre"] if "genre" in x else None, firstDataList) )
        secondGenres = set( map( lambda x: x["genre"] if "genre" in x else None, secondDataList ) ) 
        intersectionIds = firstIds & secondIds
        intersectionGenres = firstGenres & secondGenres
        self.firstData = firstDataList
        self.secondData = secondDataList
        self.commonPerformers = []

        self.genreToPerformersLists = dict()
        for genre in intersectionGenres:
            if genre:
                self.genreToPerformersLists[genre] = [[], []]

        for data in firstDataList:
            if data["id"] in intersectionIds:
                self.commonPerformers.append( data )
            if "genre" in data and data["genre"] in intersectionGenres:
                self.genreToPerformersLists[data["genre"]][0].append( data )

        for data in secondDataList:
            if "genre" in data and data["genre"] in intersectionGenres:
                self.genreToPerformersLists[data["genre"]][1].append( data )

    def process(self):

        intersections = []
        if len( self.firstData ) > MINIMAL_MUSIC_LIKES and len( self.secondData ) > MINIMAL_MUSIC_LIKES:
            intersections.append( Intersection( "Abusive love to musics", 
            abusiveLoveToMusicsDefaultWeight, (None, None), 
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
                "You seem to like", "musics. What is your favourite?")

            event = findNearestEvent( data )
            
            if event:
                loc = ""
                if "city" in event["place"]["location"]:
                    loc = " in " + event["place"]["location"]["city"]
                elif "county" in event["place"]["location"]:
                    loc = " in " + event["place"]["location"]["country"]

                goToEventSuggesion = "Hey, you like " + data["name"] \
                    + ". There will be " + event["name"] + "at " + event["place"]["name"]\
                    + loc + "." + " Do you mind going together?" 

                intersections.append( Intersection( performerTipString( data, "Like music of", "" ), 
                    suggestCommonArtistWeight, ( Content( ContentType.IMAGE_URL, pictureUrl ), None), [ 
                    Tip( confirmMutiallyLikingPerformerTip, 0.5 ), Tip( askAboutFavouritePerformerSongTip, 0.5 ),
                    Tip( goToEventSuggesion, 0.3)
                     ] ) )
            else:
                intersections.append( Intersection( performerTipString( data, "Like music of", "" ), 
                    suggestCommonArtistWeight, ( Content( ContentType.IMAGE_URL, pictureUrl ), None), [ 
                    Tip( confirmMutiallyLikingPerformerTip, 0.5 ), Tip( askAboutFavouritePerformerSongTip, 0.5 ) ] ) )

        for genre, performersPair in self.genreToPerformersLists.items():
            firstList = performersPair[0]
            secondList = performersPair[1]
            firstElement = random.choice( firstList )
            secondElement = random.choice( secondList )
            firstUrl = getCoverUrl( firstElement )
            secondUrl = getCoverUrl( secondElement )

            firstName = firstElement["name"]
            secondName = secondElement["name"]

            text = "Looks like you are listening to " + genre + " music. I also do. Have you heard about " \
                + secondName + "?"

            intersections.append( Intersection( "Like music of " + genre + ": " + firstName + ", " + secondName, 
                    suggestCommonGenreWeight, ( 
                    Content( ContentType.IMAGE_URL, firstUrl ), 
                    Content( ContentType.IMAGE_URL, secondUrl ) ), 
                    [ Tip( text, 1.0 ) ] ) )

        return intersections

    def update(self):
        pass
