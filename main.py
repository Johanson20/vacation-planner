from Recommender import *

if __name__ == "__main__":
    myPlanner = Recommender()
    api_key = input("Enter Google API key: ")
    myPlanner.gmaps = googlemaps.Client(key=api_key)

    suggestions = []
    city = input('Enter city name: ')
    print('On a scale of 1-5, rate your interest in these kind of locations (1 = not interested, 3 = neutral, 5 = very interested)' )

    for i in range(12):
        rating = input(myPlanner.categories[i] + ": ")
        suggestions.append(int(rating))

    print("These are your ranked category of sites in decreasing preference:")
    print(myPlanner.recommend(suggestions))

    places_found = myPlanner.findPlaces(suggestions, city)
    itinerary = myPlanner.showItinerary(places_found,  6)    #2-day vacation

    print("\nThe following places are recommended to visit:\n", json.dumps(itinerary, indent = 4, ensure_ascii=False))

