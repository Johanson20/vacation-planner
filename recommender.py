# install and import googlemaps api
#pip install googlemaps
import googlemaps, pickle, json
import numpy as np
import warnings
warnings.filterwarnings("ignore")

api_key = input("Enter Google API key: ")

gmaps = googlemaps.Client(key=api_key)

# reload saved kmeans data from file
file = open('C:/Users/Johanson Onyegbula/Documents/Masters in NRES/Spring 2023/CS_691/Project/vacation-planner/important', 'rb')
kmeans, Y = pickle.load(file)
file.close()

# assess cluster groups
clust_data = Y.groupby('cluster').mean()

# function to return ranked location types for user
def recommend(userdata):
    test_user = Y.loc[0:1,]
    test_user.drop(1, inplace = True)
    test_user.drop('cluster', axis=1, inplace = True)
    test_user.loc[0] = userdata
    clust = kmeans.predict(test_user)
    clust = clust_data.loc[clust[0], ].sort_values(ascending=False)
    return list(clust.index)


# function to plan itinerary of specific places within 50 miles radius of choice city from ranked location types
# default is 3 places for a 1-day vacation (give input for places as 3*vacation_length)
def show_itinerary(suggestions, city, places=6, radius = 80000):
    coords = gmaps.places(query=city)['results'][0]['geometry']['location']
    location = str(coords['lat']) + "," + str(coords['lng'])
    
    # the choices (for top 4 place types) return multiple places for each below
    choices = []
    addresses = dict()
    ratedChoices = dict()
    for i in range(4):
        choices.append(gmaps.places_nearby(location, radius, type=suggestions[i]))
    
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
                    ratedChoices[rateKey] = np.argsort(np.array(ratings))
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
    return json.dumps(addresses, indent = 4, ensure_ascii=False)


categories = ['Movie theater', 'Art gallery', 'Clothing stores', 'University', 'Bars', 'Shopping malls', 'Museum', 'Stadium', 'Zoo', 'Points of interest', 'Tourist attractions', 'Parks']
suggestions = []
city = input('Enter city name: ')
print('On a scale of 1-5, rate your interest in these kind of locations (1 = not interested, 3 = neutral, 5 = very interested)' )

for i in range(12):
    rating = input(categories[i] + ": ")
    suggestions.append(int(rating))

itinerary = show_itinerary(suggestions, city, 6)    #2-day vacation
print(itinerary)
