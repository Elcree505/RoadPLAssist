import requests
from config import settings

class POIService:
    @staticmethod
    def get_relevant_pois(location, interests, radius=10000):
        """Get POIs from Google Places"""
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "location": location,
            "radius": radius,
            "type": "point_of_interest",
            "keyword": ",".join(interests),
            "key": settings.GOOGLE_MAPS_API_KEY
        }
        response = requests.get(url, params=params).json()
        return response.get('results', [])

    @staticmethod
    def score_poi(poi, user_interests):
        """Simple scoring mechanism"""
        score = 0
        for interest in user_interests:
            if interest.lower() in poi['name'].lower():
                score += 1
        return score
