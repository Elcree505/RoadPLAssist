from geopy.geocoders import Nominatim
from geopy.distance import geodesic

_geolocator = Nominatim(user_agent="travel-assistant")

def get_coordinates(location: str) -> tuple:
    """
    Convert a location name (string) into geographic coordinates (latitude, longitude).
    """
    location_data = _geolocator.geocode(location)
    if location_data:
        return (location_data.latitude, location_data.longitude)
    else:
        raise ValueError(f"Could not geocode location: {location}")

def get_distance_km(coord1: tuple, coord2: tuple) -> float:
    """
    Return distance in kilometers between two coordinates (lat, lon).
    """
    return geodesic(coord1, coord2).km
