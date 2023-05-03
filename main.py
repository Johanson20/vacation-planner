from Recommender import Recommender
import googlemaps
import json
import ast
import warnings
import os
warnings.filterwarnings("ignore")

if __name__ == "__main__":
    myPlanner = Recommender()
    api_key = os.environ.get('arg1')
    myPlanner.gmaps = googlemaps.Client(key=api_key)

    city = os.environ.get('arg2')
    suggestions = ast.literal_eval(os.environ.get('arg3'))

    print("\nThese are your ranked category of sites in decreasing preference:")
    print(myPlanner.recommend(suggestions))

    places_found = myPlanner.findPlaces(suggestions, city)
    itinerary = myPlanner.showItinerary(places_found,  6)    #2-day vacation

    print("\nThe following places are recommended to go to:\n", 
          json.dumps(itinerary, indent = 4, ensure_ascii=False))

