from typing import List, Dict
from .intersection import Intersection
from .tip import Tip
import random
from .content import Content, ContentType
from enum import Enum, unique
from .tools import UpdateType

def tipString( data, tipBegin, tipEnd ):
    performerName = data["name"]
    return tipBegin + " " + performerName + tipEnd

def getCoverUrl( data ):
    pictureUrl = None
    if "cover" in data:
        pictureUrl = data["cover"]["source"]
    return pictureUrl

MINIMAL_MOVIES_LIKES = 20
abusiveLoveToMovieDefaultWeight = 1.0
suggestCommonMovieWeight = 0.5
suggestCommonGenreWeight = 0.3


@unique
class QuestionType(Enum):
    GENERAL_MOVIE_QUESTION = 1,
    SPECIFIC_GENERAL_QUESTION = 2,
    DISCUSS_MOVIE = 3,
    DISCUSS_SIMILAR_MOVIE = 4,
    DISCUSS_GENRE_MOVIE_SUGGESTION = 5,
    DISCUSS_GENRE_CINEMA_SUGGESTION = 6


class MovieProccessor:

    def __init__( self, firstData, secondData):
        self.movie_confidence = 0.5

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
        self.commonMovies = []

        self.genreToMoviesLists = dict()
        for genre in intersectionGenres:
            if genre:
                self.genreToMoviesLists[genre] = [[], []]

        for data in firstDataList:
            if data["id"] in intersectionIds:
                self.commonMovies.append( data )
            if "genre" in data and data["genre"] in intersectionGenres:
                self.genreToMoviesLists[data["genre"]][0].append( data )

        for data in secondDataList:
            if "genre" in data and data["genre"] in intersectionGenres:
                self.genreToMoviesLists[data["genre"]][1].append( data )

        self.idToType = dict()
        self.idToMovie = dict()

        self.lastTipId = -1

    def process(self):

        if self.movie_confidence < 0.5:
            return []

        intersections = []

        tip1 = Tip( "Do you actually like watching movies?", 1.0 )
        self.idToType[tip1.id] = QuestionType.GENERAL_MOVIE_QUESTION
        tip2 = Tip( "You seem to love movies. What is your favourite?", 0.9)
        self.idToType[tip2.id] = QuestionType.SPECIFIC_GENERAL_QUESTION
        if len( self.firstData ) > MINIMAL_MOVIES_LIKES and len( self.secondData ) > MINIMAL_MOVIES_LIKES:
            intersections.append( Intersection( "Like watching movies",
                abusiveLoveToMovieDefaultWeight, (None, None), [ tip1, tip2 ] ) )
        
        for data in self.commonMovies:
            pictureUrl = getCoverUrl( data )

            discussMovieTip = tipString( data, "What do you like about", "?" )
            discussSimilarMovieTip = tipString( data, "Do you know what movies like", " came out recently?" )

            intersections.append( Intersection( tipString( data, "Like movie", "" ), 
                suggestCommonMovieWeight, ( Content( ContentType.IMAGE_URL, pictureUrl ), None ), 
                [ Tip( discussMovieTip, 0.9 ),
                  Tip( discussSimilarMovieTip, 1.0 ) ] ) )

        for genre, moviesPair in self.genreToMoviesLists.items():
            firstList = moviesPair[0]
            secondList = moviesPair[1]
            firstElement = random.choice( firstList )
            secondElement = random.choice( secondList )
            firstUrl = getCoverUrl( firstElement )
            secondUrl = getCoverUrl( secondElement )

            firstName = firstElement["name"]
            secondName = secondElement["name"]

            if firstName != secondName:
                movieRecomendation = "Looks like you like watching " + genre + " movies. You might like " + firstName
                goingToCinemaSuggestion = "Looks like you like watching " + genre + " movies. What about going to cinema?"

                intersections.append( Intersection( "Like " + genre + " movies: " + firstName + ", " + secondName, 
                    suggestCommonGenreWeight, ( Content( ContentType.IMAGE_URL, firstUrl ), 
                    Content( ContentType.IMAGE_URL, secondUrl ) ), 
                    [ Tip( movieRecomendation, 0.9 ),
                      Tip( goingToCinemaSuggestion, 0.5 )  ] ) )

        return intersections

    def update(self, data, nlpInfo):
        if UpdateType.DELETE_TIP == data.type:
            id = data.tip_id
            pass
        elif UpdateType.INCOME_MSG == data.type:
            pass

        elif UpdateType.OUTCOME_MSG == data.type:
            pass
        elif UpdateType.OUTCOME_TIP_MSG == data.type:
            self.lastTipId = data.tip_id
            pass
