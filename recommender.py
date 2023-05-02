# install and import googlemaps api
#pip install googlemaps
import os, googlemaps, pickle, json
import warnings, pandas, sklearn
warnings.filterwarnings("ignore")


class Recommender:
    def __init__(self):
        self.gmaps = None
        self.categories = ['Movie theater', 'Art gallery', 'Clothing stores', 'University', 'Bars', 'Shopping malls', 'Museum', 'Stadium', 'Zoo', 'Points of interest', 'Tourist attractions', 'Parks']
        file = open('important', 'rb')
        kmeans, Y = pickle.load(file)
        file.close()
        self.test_user = Y.loc[0:1,]
        self.test_user.drop(1, inplace = True)
        self.test_user.drop('cluster', axis=1, inplace = True)
        self.kmeans = kmeans
        self.reviews_data = Y
        self.clust_data = self.reviews_data.groupby('cluster').mean()

    # method to return ranked location types for user
    def recommend(self, userdata):
        self.test_user.loc[0] = userdata
        clust = self.kmeans.predict(self.test_user)
        clust = self.clust_data.loc[clust[0], ].sort_values(ascending=False)
        return list(clust.index)

    # method to find locations by category type (default of 5 mile radius)
    def findLocationByType(self, city, category, radius=8000):
        coords = self.gmaps.places(query=city)['results'][0]['geometry']['location']
        location = str(coords['lat']) + "," + str(coords['lng'])
        
        places = self.gmaps.places_nearby(location, radius, type=category)
        return places
        
    #method to find specific places within 50 miles radius (in meters) of choice city from ranked location types
    def findPlaces(self, suggestions, city, radius = 80000):
        coords = self.gmaps.places(query=city)['results'][0]['geometry']['location']
        location = str(coords['lat']) + "," + str(coords['lng'])
        
        # the choices (for top 4 place types) return multiple places for each below
        choices = []
        for i in range(4):
            choices.append(self.gmaps.places_nearby(location, radius, type=suggestions[i]))
        return choices
    
    # method to plan itinerary: default is 3 places for a 1-day vacation (give input for places as 3*vacation_length)
    def showItinerary(self, choices, places=6):
        addresses = dict()
        ratedChoices = dict()
        
        # populate addresses of top destinations according to rating and recommended type
        j = 0
        while j < places:
            for i in range(len(choices)):
                k = 0
                if 'results' in choices[i] and len(choices[i]['results']) > 0:
                    choice = choices[i]['results']
                    rateKey = 'choice' + str(i)
                    if rateKey not in ratedChoices:
                        ratings = [choice[i]['rating'] for i in range(len(choice)) if 'rating' in choice[i]]
                        ratings = [[ratings[i], i] for i in range(len(ratings))]
                        ratings = sorted(ratings)
                        ratedChoices[rateKey] = [value[1] for value in ratings]
                    if len(ratedChoices[rateKey]) > 0:
                        mylocation = choice[ratedChoices[rateKey][k]]
                        while mylocation['name'] in addresses:
                            k += 1
                            mylocation = choice[ratedChoices[rateKey][k]]
                        addresses[mylocation['name']] = mylocation['vicinity']
                        ratedChoices[rateKey] = ratedChoices[rateKey][1:]
                        j += 1
        
        addresses = [[value[0], value[1]] for value in addresses.items()]
        addresses = addresses[0:places]    
        return addresses
