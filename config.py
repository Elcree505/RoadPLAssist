import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    GOOGLE_MAPS_API_KEY: str
    WEATHER_API_KEY: str
    MAX_POIS: int = 10
    OPTIMIZATION_THRESHOLD: float = 0.8  # 80% of max score

settings = Settings()
