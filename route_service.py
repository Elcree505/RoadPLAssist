import requests
from geopy.distance import geodesic
from config import settings
from geopy_utils import get_coordinates

class RouteService:
    @staticmethod
    def get_directions(origin, destination):
        """Get directions using Google Maps API"""
        url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": origin,
            "destination": destination,
            "key": settings.GOOGLE_MAPS_API_KEY
        }
        response = requests.get(url, params=params).json()
        return response['routes'][0]['legs'][0] if response['routes'] else None

    @staticmethod
    def calculate_distance(loc1, loc2):
        """Calculate distance between two locations"""
        coords1 = get_coordinates(loc1)
        coords2 = get_coordinates(loc2)
        return geodesic(coords1, coords2).miles
