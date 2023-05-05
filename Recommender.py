import pickle
import warnings
warnings.filterwarnings("ignore")


class Recommender:
    def __init__(self):
        file = open('important', 'rb')
        self.kmeans, self.reviews_data = pickle.load(file)
        file.close()
        self.test_user = self.reviews_data.loc[0:1,]
        self.test_user.drop(1, inplace = True)
        self.test_user.drop('cluster', axis=1, inplace = True)
        self.clust_data = self.reviews_data.groupby('cluster').mean()

    # method to return ranked location types for user
    def recommend(self, userdata):
        self.test_user.loc[0] = userdata
        clust = self.kmeans.predict(self.test_user)
        clust = self.clust_data.loc[clust[0], ].sort_values(ascending=False)
        return list(clust.index)
    
    #method to find specific places from ranked location types
    def findPlaces(self, suggestion, city, places):
        choices = []
        for i in range(len(places)):
            for j in range(len(places[i]['results'])):
                example = places[i]['results'][j]
                if suggestion in example['types']:
                    choices.append(example)
        return choices
    
    # method to plan itinerary: default is 3 places for a 1-day vacation 
    # (give input for places as 3*vacation_length)
    def showItinerary(self, choices, places=6):
        addresses = dict()
        ratedChoices = dict()
        
        # populate addresses of top destinations according to rating
        j = 0
        while j < places:
            for i in range(len(choices)):
                k = 0
                if 'results' in choices[i] and len(choices[i]['results']) > 0:
                    choice = choices[i]['results']
                    rateKey = 'choice' + str(i)
                    if rateKey not in ratedChoices:
                        ratings = [choice[i]['rating'] for i in range(len(choice))
                                    if 'rating' in choice[i]]
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
