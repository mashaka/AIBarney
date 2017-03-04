from typing import List, Dict
from .intersection import Intersection
from .tip import Tip
import random

def tipString( data, tipBegin, tipEnd ):
    performerName = data["name"]
    
    return tipBegin + " " + performerName + " " + tipEnd

def getCoverUrl( data ):
    pictureUrl = None
    if data["cover"]:
        pictureUrl = data["cover"]["source"]
    return pictureUrl

MINIMAL_MOVIES_LIKES = 50
abusiveLoveToMovieDefaultWeight = 0.1
suggestCommonMovieWeight = 0.5
suggestCommonGenreWeight = 0.3

class MovieProccessor:

    def __init__( firstDataList: List[Dict], secondDataList: List[Dict] ):
        firstIds = set( map( lambda x: x["id"], firstDataList ) )
        secondIds = set( map( lambda x: x["id"], secondDataList ) )
        firstGenres = set( map( lambda x: x["genre"], firstDataList) )
        secondGenres = set( map( lambda x: x["genre"], secondDataList ) ) 
        intersectionIds = firstIds & secondIds
        intersectionGenres = firstGenres & secondGenres
        self.firstData = firstDataList
        self.secondData = secondDataList
        self.commonMovies = []

        self.genreToMoviesLists = dict()
        for genre in intersectionGenres:
            self.genreToMoviesLists[genre] = [[], []]

        for data in firstDataList:
            if data["id"] in intersectionIds:
                self.commonMovies.append( data )
            if data["genre"] in intersectionGenres:
                self.genreToMoviesLists[data["genre"]][0].append( data )

        for data in secondDataList:
            if data["genre"] in intersectionGenres:
                self.genreToMoviesLists[data["genre"]][1].append( data )

    def process():

        intersections = []
        if len( self.firstData ) > MINIMAL_MOVIES_LIKES and len( self.secondData ) > MINIMAL_MOVIES_LIKES:
            intersections.append( Intersection( "Like watching movies", 
            abusiveLoveToMusicsDefaultWeight, [None, None], 
            [
                Tip( "Do you actually like watching movies?", 1.0 ),
                Tip( "You seem to love movies. What is your favourite?", 0.9 )
            ],
            0.1 ) )
        
        for data in self.commonMovies:
            pictureUrl = getCoverUrl( data )

            discussMovieTip = tipString( data, "What do you like about movie", "?" )
            discussSimilarMovieTip = tipString( data, "Do you know what movies like", "came out recently?" )

            intersections.append( Intersection( tipString( data, "Like movie", "" ), 
                suggestCommonArtistWeight, [pictureUrl, None], [ Tip( discussMovieTip, 0.9 ),
                Tip( discussSimilarMovieTip, 1.0 ) ] ) )

        for genre, moviesPair in self.genreToMoviesLists:
            firstList = moviesPair[0]
            secondList = moviesPair[1]
            firstElement = random.choice( firstList )
            secondElement = random.choice( secondList )
            firstUrl = getCoverUrl( firstElement )
            secondUrl = getCoverUrl( secondElement )

            firstName = firstElement["name"]
            secondName = secondElement["name"]


            movieRecomendation = "Looks like you like watching " + genre + " movies. You might like " + firstName
            goingToCinemaSuggestion = "Looks like you like watching " + genre + " movies. What about going to cinema?"

            intersections.append( Intersection( "Like " + genre + " movies: " + firstName + ", " + secondName, 
                suggestCommonGenreWeight, [ firstUrl, secondUrl ], [ Tip( movieRecomendation, 0.9 ),
                Tip( goingToCinemaSuggestion, 0.5 )  ] ) )

    def update():
        pass