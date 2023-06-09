from Recommender import Recommender
import unittest
from unittest.mock import Mock
import warnings
warnings.filterwarnings("ignore")


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.myPlanner = Recommender()
        
        self.myplaces = [{'results': [{'geometry': {'location': {'lat': 39.529919,
              'lng': -119.8142691},
             'viewport': {'northeast': {'lat': 39.72343600972929,
               'lng': -119.6993449394376},
              'southwest': {'lat': 39.39242607073351, 'lng': -120.0023379138833}}},
            'name': 'Reno',
            'place_id': 'ChIJnaCSkq5AmYARh_c4dM7FxUA',
            'reference': 'ChIJnaCSkq5AmYARh_c4dM7FxUA',
            'scope': 'GOOGLE',
            'types': ['locality', 'political'],
            'vicinity': 'Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.5304918, 'lng': -119.8149946},
             'viewport': {'northeast': {'lat': 39.5319129302915,
               'lng': -119.8140769197085},
              'southwest': {'lat': 39.5292149697085, 'lng': -119.8167748802915}}},
            'name': 'Silver Legacy Resort Casino',
            'place_id': 'ChIJRYQdLTRHmYARu8Op-jB28TE',
            'plus_code': {'compound_code': 'G5JP+52 Reno, NV, USA',
             'global_code': '85F2G5JP+52'},
            'rating': 4.2,
            'reference': 'ChIJRYQdLTRHmYARu8Op-jB28TE',
            'scope': 'GOOGLE',
            'types': ['casino', 'lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 15141,
            'vicinity': '407 North Virginia Street, Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.5291595, 'lng': -119.8146488},
             'viewport': {'northeast': {'lat': 39.53055498029149,
               'lng': -119.81316105},
              'southwest': {'lat': 39.52785701970849, 'lng': -119.81606765}}},
            'name': 'Eldorado Resort Casino',
            'place_id': 'ChIJ080StzVHmYARD-YbD1sKARw',
            'plus_code': {'compound_code': 'G5HP+M4 Reno, NV, USA',
             'global_code': '85F2G5HP+M4'},
            'rating': 4.2,
            'reference': 'ChIJ080StzVHmYARD-YbD1sKARw',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 11693,
            'vicinity': '345 North Virginia Street, Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.5314464, 'lng': -119.8157093},
             'viewport': {'northeast': {'lat': 39.53276483029149, 'lng': -119.8139715},
              'southwest': {'lat': 39.5300668697085, 'lng': -119.8169571}}},
            'name': 'Circus Circus Reno',
            'place_id': 'ChIJ8ZZtmjZHmYARPmy0CY53NYo',
            'plus_code': {'compound_code': 'G5JM+HP Reno, NV, USA',
             'global_code': '85F2G5JM+HP'},
            'rating': 4.1,
            'reference': 'ChIJ8ZZtmjZHmYARPmy0CY53NYo',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 15543,
            'vicinity': '500 North Sierra Street, Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.5281442, 'lng': -119.8188873},
             'viewport': {'northeast': {'lat': 39.52950208029149,
               'lng': -119.8173934197085},
              'southwest': {'lat': 39.52680411970849, 'lng': -119.8200913802915}}},
            'name': 'J Resort',
            'opening_hours': {'open_now': True},
            'place_id': 'ChIJBzXVmTNHmYAR6ipRaf8zVCE',
            'plus_code': {'compound_code': 'G5HJ+7C Reno, NV, USA',
             'global_code': '85F2G5HJ+7C'},
            'rating': 3.5,
            'reference': 'ChIJBzXVmTNHmYAR6ipRaf8zVCE',
            'scope': 'GOOGLE',
            'types': ['casino', 'lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 6758,
            'vicinity': '345 North Arlington Avenue, Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.5230411, 'lng': -119.7812235},
             'viewport': {'northeast': {'lat': 39.5243317802915,
               'lng': -119.7796759697085},
              'southwest': {'lat': 39.5216338197085, 'lng': -119.7823739302915}}},
            'name': 'Grand Sierra Resort',
            'opening_hours': {'open_now': True},
            'place_id': 'ChIJG7qnuls_mYARweP739kMgh8',
            'plus_code': {'compound_code': 'G6F9+6G Reno, NV, USA',
             'global_code': '85F2G6F9+6G'},
            'rating': 4.3,
            'reference': 'ChIJG7qnuls_mYARweP739kMgh8',
            'scope': 'GOOGLE',
            'types': ['casino',
             'movie_theater',
             'night_club',
             'bar',
             'lodging',
             'restaurant',
             'point_of_interest',
             'food',
             'establishment'],
            'user_ratings_total': 25236,
            'vicinity': '2500 East 2nd Street, Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.513984, 'lng': -119.782839},
             'viewport': {'northeast': {'lat': 39.51521228029151,
               'lng': -119.7812296197085},
              'southwest': {'lat': 39.51251431970851, 'lng': -119.7839275802915}}},
            'name': 'Holiday Inn Express & Suites Reno Airport, an IHG Hotel',
            'place_id': 'ChIJX8m41WY_mYAR7oBrdT7oP9M',
            'plus_code': {'compound_code': 'G678+HV Reno, NV, USA',
             'global_code': '85F2G678+HV'},
            'rating': 4.4,
            'reference': 'ChIJX8m41WY_mYAR7oBrdT7oP9M',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 574,
            'vicinity': '2375 Market Street, Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.4976865, 'lng': -119.801139},
             'viewport': {'northeast': {'lat': 39.50067119999999,
               'lng': -119.79638035},
              'southwest': {'lat': 39.49357520000001, 'lng': -119.80562295}}},
            'name': 'Peppermill Resort Spa Casino',
            'opening_hours': {'open_now': True},
            'place_id': 'ChIJ07LkRY9AmYARbPPabWOgb1I',
            'plus_code': {'compound_code': 'F5XX+3G Reno, NV, USA',
             'global_code': '85F2F5XX+3G'},
            'rating': 4.4,
            'reference': 'ChIJ07LkRY9AmYARbPPabWOgb1I',
            'scope': 'GOOGLE',
            'types': ['casino',
             'spa',
             'lodging',
             'restaurant',
             'point_of_interest',
             'food',
             'establishment'],
            'user_ratings_total': 19672,
            'vicinity': '2707 South Virginia Street, Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.5341343, 'lng': -119.7995919},
             'viewport': {'northeast': {'lat': 39.53553409999999, 'lng': -119.7965838},
              'southwest': {'lat': 39.5322041, 'lng': -119.8019754}}},
            'name': 'Ramada by Wyndham Reno Hotel & Casino',
            'opening_hours': {'open_now': True},
            'place_id': 'ChIJY5H7s6SZ7ocRo0_nWCZdZj0',
            'plus_code': {'compound_code': 'G6M2+M5 Reno, NV, USA',
             'global_code': '85F2G6M2+M5'},
            'rating': 3,
            'reference': 'ChIJY5H7s6SZ7ocRo0_nWCZdZj0',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 1886,
            'vicinity': '1000 East 6th Street, Reno'},
           {'business_status': 'OPERATIONAL',
            'geometry': {'location': {'lat': 39.5228373, 'lng': -119.8138873},
             'viewport': {'northeast': {'lat': 39.5243296802915,
               'lng': -119.8125708697085},
              'southwest': {'lat': 39.5216317197085, 'lng': -119.8152688302915}}},
            'name': 'Legacy Vacation Resort Reno',
            'place_id': 'ChIJQxzyRspAmYARBwUtZLSTGHw',
            'plus_code': {'compound_code': 'G5FP+4C Reno, NV, USA',
             'global_code': '85F2G5FP+4C'},
            'rating': 3.3,
            'reference': 'ChIJQxzyRspAmYARBwUtZLSTGHw',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 591,
            'vicinity': '140 Court Street, Reno'}],
          'status': 'OK'},
         {'results': [{'name': 'Reno',
            'place_id': 'ChIJnaCSkq5AmYARh_c4dM7FxUA',
            'reference': 'ChIJnaCSkq5AmYARh_c4dM7FxUA',
            'scope': 'GOOGLE',
            'types': ['locality', 'political'],
            'vicinity': 'Reno'},
           {'name': 'Silver Legacy Resort Casino',
            'place_id': 'ChIJRYQdLTRHmYARu8Op-jB28TE',
            'plus_code': {'compound_code': 'G5JP+52 Reno, NV, USA',
             'global_code': '85F2G5JP+52'},
            'rating': 4.2,
            'reference': 'ChIJRYQdLTRHmYARu8Op-jB28TE',
            'scope': 'GOOGLE',
            'types': ['casino', 'lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 15141,
            'vicinity': '407 North Virginia Street, Reno'},
           {'name': 'Eldorado Resort Casino',
            'place_id': 'ChIJ080StzVHmYARD-YbD1sKARw',
            'plus_code': {'compound_code': 'G5HP+M4 Reno, NV, USA',
             'global_code': '85F2G5HP+M4'},
            'rating': 4.2,
            'reference': 'ChIJ080StzVHmYARD-YbD1sKARw',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 11693,
            'vicinity': '345 North Virginia Street, Reno'},
           {'name': 'Circus Circus Reno',
            'place_id': 'ChIJ8ZZtmjZHmYARPmy0CY53NYo',
            'plus_code': {'compound_code': 'G5JM+HP Reno, NV, USA',
             'global_code': '85F2G5JM+HP'},
            'rating': 4.1,
            'reference': 'ChIJ8ZZtmjZHmYARPmy0CY53NYo',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 15543,
            'vicinity': '500 North Sierra Street, Reno'},
           {'name': 'J Resort',
            'opening_hours': {'open_now': True},
            'place_id': 'ChIJBzXVmTNHmYAR6ipRaf8zVCE',
            'plus_code': {'compound_code': 'G5HJ+7C Reno, NV, USA',
             'global_code': '85F2G5HJ+7C'},
            'rating': 3.5,
            'reference': 'ChIJBzXVmTNHmYAR6ipRaf8zVCE',
            'scope': 'GOOGLE',
            'types': ['casino', 'lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 6758,
            'vicinity': '345 North Arlington Avenue, Reno'},
           {'name': 'Grand Sierra Resort',
            'opening_hours': {'open_now': True},
            'place_id': 'ChIJG7qnuls_mYARweP739kMgh8',
            'plus_code': {'compound_code': 'G6F9+6G Reno, NV, USA',
             'global_code': '85F2G6F9+6G'},
            'rating': 4.3,
            'reference': 'ChIJG7qnuls_mYARweP739kMgh8',
            'scope': 'GOOGLE',
            'types': ['casino',
             'night_club',
             'bar',
             'movie_theater',
             'lodging',
             'restaurant',
             'food',
             'point_of_interest',
             'establishment'],
            'user_ratings_total': 25236,
            'vicinity': '2500 East 2nd Street, Reno'},
           {'name': 'Holiday Inn Express & Suites Reno Airport, an IHG Hotel',
            'place_id': 'ChIJX8m41WY_mYAR7oBrdT7oP9M',
            'plus_code': {'compound_code': 'G678+HV Reno, NV, USA',
             'global_code': '85F2G678+HV'},
            'rating': 4.4,
            'reference': 'ChIJX8m41WY_mYAR7oBrdT7oP9M',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 574,
            'vicinity': '2375 Market Street, Reno'},
           {'name': 'Peppermill Resort Spa Casino',
            'opening_hours': {'open_now': True},
            'place_id': 'ChIJ07LkRY9AmYARbPPabWOgb1I',
            'plus_code': {'compound_code': 'F5XX+3G Reno, NV, USA',
             'global_code': '85F2F5XX+3G'},
            'rating': 4.4,
            'reference': 'ChIJ07LkRY9AmYARbPPabWOgb1I',
            'scope': 'GOOGLE',
            'types': ['casino',
             'spa',
             'lodging',
             'restaurant',
             'food',
             'point_of_interest',
             'establishment'],
            'user_ratings_total': 19672,
            'vicinity': '2707 South Virginia Street, Reno'},
           {'name': 'Ramada by Wyndham Reno Hotel & Casino',
            'opening_hours': {'open_now': True},
            'place_id': 'ChIJY5H7s6SZ7ocRo0_nWCZdZj0',
            'plus_code': {'compound_code': 'G6M2+M5 Reno, NV, USA',
             'global_code': '85F2G6M2+M5'},
            'rating': 3,
            'reference': 'ChIJY5H7s6SZ7ocRo0_nWCZdZj0',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 1886,
            'vicinity': '1000 East 6th Street, Reno'},
           {'name': 'Legacy Vacation Resort Reno',
            'place_id': 'ChIJQxzyRspAmYARBwUtZLSTGHw',
            'plus_code': {'compound_code': 'G5FP+4C Reno, NV, USA',
             'global_code': '85F2G5FP+4C'},
            'rating': 3.3,
            'reference': 'ChIJQxzyRspAmYARBwUtZLSTGHw',
            'scope': 'GOOGLE',
            'types': ['lodging', 'point_of_interest', 'establishment'],
            'user_ratings_total': 591,
            'vicinity': '140 Court Street, Reno'}],
          'status': 'OK'}]
        
    def test_recommend(self):
        self.assertEqual(self.myPlanner.recommend([3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 4])
                [0:4], ['shopping_mall', 'movie_theater', 
            'art_gallery', 'clothing_store'])
    
    def test_findPlaces(self):
        self.assertEqual(len(self.myPlanner.findPlaces('movie_theater', 'Reno', 
            self.myplaces)), 2)
    
    def test_showItinerary(self):
        self.assertNotEqual(self.myPlanner.showItinerary(self.myplaces)[0], 
            ['Legacy Vacation Resort Reno', '140 Court Street, Reno'])

    def test_showSanFranciscoItinerary(self):
        sfVac = Mock()
        sfVac.findPlaces.return_value = self.myplaces
        places = sfVac.findPlaces([5, 5, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3],
                 "San Francisco")
        self.assertNotEqual(self.myPlanner.showItinerary(places)[1:3], 
            [['Edwardian Hotel', '1668 Market Street, San Francisco'], 
             ['Hayes Valley Inn', '417 Gough Street, San Francisco']])
    
    def test_RenoStadiumItinerary(self):
        renoVac = Mock()
        renoVac.findPlaces.return_value = self.myplaces
        stadia = self.myPlanner.recommend([1, 2, 1, 3, 2, 3, 3, 5, 2, 3, 3, 3])
        self.assertEqual(renoVac.findPlaces(stadia, 'Reno')[0]['results']
                         [1]['vicinity'], 
            '407 North Virginia Street, Reno')
    
    def test_ParkItineraryInArizona(self):
        azVac = Mock()
        azVac.findPlaces.return_value = self.myplaces
        top_choice = self.myPlanner.recommend([5, 1, 1, 1, 5, 1, 1, 1, 1, 5, 1, 1])
        parks = azVac.findPlaces(top_choice, 'Prescott')
        self.assertNotEqual(self.myPlanner.showItinerary(parks, 3), 
                         [['Butte Creek Trail', '1750 Sherwood Drive, Prescott'], 
            ['Picture Show at Frontier Village', '1771E Arizona 69, Prescott'], 
            ['Heritage Park Zoological Sanctuary', 
            '1403 Heritage Park Road, Prescott']])
    
    def test_ArtGalleryInChicago(self):
        chicago = Mock()
        chicago.findPlaces.return_value = self.myplaces
        top_choice = self.myPlanner.recommend([3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2])
        choices = chicago.findPlaces(top_choice, "Chicago")
        self.assertNotEqual(self.myPlanner.showItinerary(choices, 3)[1], 
            ['Simply Thalia', '108 North State Street, Chicago'])
    
    def test_EmptyUniversityInCarson(self):
        chesapeake = Mock()
        chesapeake.findPlaces.return_value = []
        preference = self.myPlanner.recommend([1, 1, 2, 1, 2, 2, 2, 5, 1, 2, 1, 1])[0]
        choices = chesapeake.findPlaces("Chesapeake Bay", preference)
        self.assertEqual(len(choices), 0)


if __name__ == '__main__':
    unittest.main()
