import unittest
from Recommender import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.myPlanner = Recommender()
        self.myPlanner.gmaps = googlemaps.Client(key='AIzaSyDBO8sGBqk8aAs9OhvTdpsr0rSEURemOVk')
        self.myplaces = self.myPlanner.findPlaces([3, 3, 3, 5, 3, 3, 3, 3, 5, 3, 3, 3], "Reno", 1600)
    
    def test_recommend(self):
        self.assertEqual(self.myPlanner.recommend([3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 4]), ['shopping_mall', 'movie_theater', 'art_gallery', 'clothing_store', 'university', 'bar', 'museum', 'stadium', 'zoo', 'point_of_interest', 'tourist_attraction', 'park'])
    
    def test_findLocationByType(self):
        self.assertEqual(self.myPlanner.findLocationByType("Las Vegas", "restaurant", 1000)['results'][0]['vicinity'], '129 East Fremont Street, Las Vegas')
        
    def test_findPlaces(self):
        self.assertEqual(self.myPlanner.findPlaces([5, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3], "Reno", 40000)[0]['results'][1]['vicinity'], '407 North Virginia Street, Reno')

    def test_showItinerary(self):
        self.assertEqual(self.myPlanner.showItinerary(self.myplaces)[0], ['Legacy Vacation Resort Reno', '140 Court Street, Reno'])

    def test_showSanFranciscoItinerary(self):
        places = self.myPlanner.findPlaces([5, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3], "San Francisco")
        self.assertEqual(self.myPlanner.showItinerary(places)[1:3], [['Edwardian Hotel', '1668 Market Street, San Francisco'], ['Hayes Valley Inn', '417 Gough Street, San Francisco']])
    
    def test_RenoStadiumItinerary(self):
        self.assertEqual(self.myPlanner.findPlaces('Reno', self.myPlanner.recommend([1, 2, 1, 3, 2, 3, 3, 5, 2, 3, 3, 3])[0])[0]['results'][1]['vicinity'], '500 North Sierra Street, Reno')
    
    def test_ParkItineraryInArizona(self):
        top_choice = self.myPlanner.recommend([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5])
        parks = self.myPlanner.findPlaces(top_choice, "Prescott")
        self.assertEqual(self.myPlanner.showItinerary(parks, 3), [['Butte Creek Trail', '1750 Sherwood Drive, Prescott'], ['Picture Show at Frontier Village', '1771E Arizona 69, Prescott'], ['Heritage Park Zoological Sanctuary', '1403 Heritage Park Road, Prescott']])
        
    def test_ArtGalleryInChicago(self):
        top_choice = self.myPlanner.recommend([3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2])
        choices = self.myPlanner.findPlaces(top_choice, "Chicago")
        self.assertNotEqual(self.myPlanner.showItinerary(choices, 3)[1], ['Simply Thalia', '108 North State Street, Chicago'])
    
    def test_EmptyUniversityInCarson(self):
        preference = self.myPlanner.recommend([1, 1, 2, 1, 2, 2, 2, 5, 1, 2, 1, 1])[0]
        choices = self.myPlanner.findLocationByType("Chesapeake Bay", preference)
        self.assertNotEqual(len(choices), 1)


if __name__ == '__main__':
    unittest.main()
