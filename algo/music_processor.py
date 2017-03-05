from typing import List, Dict
from .intersection import Intersection
from .tip import Tip
import random
from datetime import datetime
from .content import Content, ContentType
from enum import Enum, unique
from .tools import UpdateType


def performerTipString(data, tipBegin, tipEnd):
    performerName = data["name"]
    return tipBegin + " " + performerName + tipEnd

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


MINIMAL_MUSIC_LIKES = 20
suggestCommonArtistWeight = 0.5
suggestCommonGenreWeight = 0.3

@unique
class QuestionType(Enum):
    GENERAL_MUSIC_QUESTION = 1,
    SPECIFIC_GENERAL_QUESTION = 2,
    PERFORMER_LIKING_QUESTION = 3,
    SPECIFIC_PERFORMER_QUESTION = 4,
    ASK_PERFORMER_EVENT = 5,
    GENRE_SUGGEST_ANOTHER = 6

class MusicProccessor:

    def __init__( self, firstData, secondData):
        self.music_confidence = 0.5
        self.abusiveLoveToMusicsDefaultWeight = 0.1
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

        self.performersWeights = dict()

        for data in firstDataList:
            if data["id"] in intersectionIds:
                self.commonPerformers.append( data )
                self.performersWeights[data["id"]] = 0.5
            if "genre" in data and data["genre"] in intersectionGenres:
                self.genreToPerformersLists[data["genre"]][0].append( data )

        for data in secondDataList:
            if "genre" in data and data["genre"] in intersectionGenres:
                self.genreToPerformersLists[data["genre"]][1].append( data )

        self.idToType = dict()
        self.idToPerformer = dict()

        self.lastTipId = -1

        self.process1()

    def process1(self):

        if self.music_confidence == 0:
            return []

        intersections = []
        if self.abusiveLoveToMusicsDefaultWeight > 0:
            firstTip = Tip( "I have seen a lot of likes on your facebook page. Do you actually like hearing musics?", 
                self.abusiveLoveToMusicsDefaultWeight )

            self.idToType[firstTip.id] = QuestionType.GENERAL_MUSIC_QUESTION


            secondTip = Tip( "You seem to love musics, there are huge amount of likes on your facebook page. What is your favourite band?", 
                self.abusiveLoveToMusicsDefaultWeight )
            self.idToType[secondTip.id] = QuestionType.SPECIFIC_GENERAL_QUESTION    


            if len( self.firstData ) > MINIMAL_MUSIC_LIKES and len( self.secondData ) > MINIMAL_MUSIC_LIKES:
                intersections.append( Intersection( "Abusive love to musics", 
                self.abusiveLoveToMusicsDefaultWeight, (None, None), 
                [
                    firstTip,
                    secondTip
                ] ) )
        
        for data in self.commonPerformers:
            id = data["id"]

            print( id )
            print( self.performersWeights[id] )

            if self.performersWeights[id] < 0.5:
                continue

            pictureUrl = getCoverUrl( data )
            
            confirmMutiallyLikingPerformerTip = performerTipString( data, 
                "You seem to hear music a lot. Do you actually like", " songs?")
            askAboutFavouritePerformerSongTip = performerTipString( data, 
                "You seem to like", " musics. What is your favorite song?" )
            
            tip1 = Tip( confirmMutiallyLikingPerformerTip, 0.9 )
            self.idToType[tip1.id] = QuestionType.PERFORMER_LIKING_QUESTION
            tip2 = Tip( askAboutFavouritePerformerSongTip, 0.7 )
            self.idToType[tip2.id] = QuestionType.SPECIFIC_PERFORMER_QUESTION
            
            self.idToPerformer[tip1.id] = id
            self.idToPerformer[tip2.id] = id

            event = findNearestEvent( data )
            print(event)
            tipsList = [ tip1, tip2 ]

            if self.performersWeights[id] > 0.6 and event:
                loc = ""
                if "city" in event["place"]["location"]:
                    loc = " in " + event["place"]["location"]["city"]
                elif "county" in event["place"]["location"]:
                    loc = " in " + event["place"]["location"]["country"]

                goToEventSuggesion = "Hey, you like " + data["name"] \
                    + ". There will be " + event["name"] + "at " + event["place"]["name"]\
                    + loc + "." + " Do you mind going together?" 

                tip3 = Tip( goToEventSuggesion, 0.5 )
                self.idToType[tip3.id] = QuestionType.ASK_PERFORMER_EVENT

                self.idToPerformer[tip3.id] = id

                tipsList.append( tip3 )
                
            intersections.append( Intersection( performerTipString( data, "Like music of", "" ), 
                suggestCommonArtistWeight, ( Content( ContentType.IMAGE_URL, pictureUrl ), None), tipsList ) )

            print( tipsList )

        for genre, performersPair in self.genreToPerformersLists.items():
            firstList = performersPair[0]
            secondList = performersPair[1]
            firstElement = random.choice( firstList )
            secondElement = random.choice( secondList )
            firstUrl = getCoverUrl( firstElement )
            secondUrl = getCoverUrl( secondElement )

            firstName = firstElement["name"]
            secondName = secondElement["name"]

            if firstName != secondName:

                text = "Looks like you are listening to " + genre + " music. I also do. Have you heard about " \
                    + secondName + "?"
                
                tip = Tip( text, 1.0 )

                self.idToType[tip.id] = QuestionType.GENRE_SUGGEST_ANOTHER

                intersections.append( Intersection( "Like music of " + genre + ": " + firstName + ", " + secondName, 
                        suggestCommonGenreWeight, ( 
                        Content( ContentType.IMAGE_URL, firstUrl ), 
                        Content( ContentType.IMAGE_URL, secondUrl ) ), 
                        [ tip ] ) )
        self.inters = intersections

    def process(self):
        return self.inters

    def update(self, data, nlpInfo):
        print( self.idToType )
        if UpdateType.DELETE_TIP == data.type:
            id = data.tip_id
            if id in self.idToType:
                print( "Delete " + str( id ) )
                tp = self.idToType[id]
                if tp == QuestionType.GENERAL_MUSIC_QUESTION or tp == QuestionType.SPECIFIC_GENERAL_QUESTION:
                    self.abusiveLoveToMusicsDefaultWeight = 0.0
                else:
                    performer = self.idToPerformer[id]
                    self.performersWeights[performer] = 0.0
        elif UpdateType.INCOME_MSG == data.type:
            flag = nlpInfo.is_positive
            print( self.performersWeights )
            print(flag)
            if data.msg == "Yes":
                flag = True
            if data.msg == "No":
                flag = False
            print(self.lastTipId)
            if self.lastTipId != -1 and self.lastTipId in self.idToType:
                tp = self.idToType[self.lastTipId]
                if tp == QuestionType.GENERAL_MUSIC_QUESTION:
                    if flag == True:
                        self.music_confidence = 1.0
                    elif flag == False:
                        self.music_confidence = 0.0
                if tp == QuestionType.PERFORMER_LIKING_QUESTION or tp == QuestionType.SPECIFIC_PERFORMER_QUESTION:
                    if flag == True:
                        self.performersWeights[ self.idToPerformer[self.lastTipId] ] = 1.0
                    elif flag == False:
                        self.performersWeights[ self.idToPerformer[self.lastTipId] ] = 0.0
                if tp == QuestionType.GENERAL_MUSIC_QUESTION or tp == QuestionType.SPECIFIC_GENERAL_QUESTION:
                    self.abusiveLoveToMusicsDefaultWeight = 0.0
            print( self.performersWeights )

        elif UpdateType.OUTCOME_MSG == data.type:
            pass
        elif UpdateType.OUTCOME_TIP_MSG == data.type:
            self.lastTipId = data.tip_id

        self.process1()
