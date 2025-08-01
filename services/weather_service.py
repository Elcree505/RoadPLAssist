import requests
from app.config import settings

class WeatherService:
    @staticmethod
    def get_weather(location):
        """Get weather data from OpenWeatherMap"""
        url = "https://api.tomorrow.io/v4/weather/forecast"
        params = {
            "q": location,
            "appid": settings.WEATHER_API_KEY
        }
        response = requests.get(url, params=params).json()
        return {
            "temp": response['main']['temp'],
            "condition": response['weather'][0]['description']
        }
