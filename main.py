from Recommender import Recommender
import googlemaps
import json
import ast
import os
import warnings
warnings.filterwarnings("ignore")

if __name__ == "__main__":
    myPlanner = Recommender()
    api_key = os.environ.get('arg1')
    gmaps = googlemaps.Client(key=api_key)
    
    city = os.environ.get('arg2')
    suggestions = ast.literal_eval(os.environ.get('arg3'))

    print("\nThese are your ranked category of sites in decreasing preference:")
    print(myPlanner.recommend(suggestions))
        
    # find specific places within 50 miles radius (in meters) 
    coords = gmaps.places(query=city)['results'][0]['geometry']['location']
    location = str(coords['lat']) + "," + str(coords['lng'])
    
    # the choices (for top 4 place types) return multiple places for each below
    places_found = []
    for i in range(4):
        places_found.append(gmaps.places_nearby(location,80000,type=suggestions[i]))
    
    itinerary = myPlanner.showItinerary(places_found,  6)    #2-day vacation

    print("\nThe following places are recommended to go to:\n", 
          json.dumps(itinerary, indent = 4, ensure_ascii=False))
