from pydantic import BaseModel
from typing import List, Optional

class UserPreferences(BaseModel):
    budget: float
    interests: List[str]
    dietary_restrictions: List[str] = []
    max_driving_time: int  # hours
    vehicle_type: str = "standard"  # standard/ev

class TravelRequest(BaseModel):
    start_location: str
    end_location: str
    trip_days: int
    preferences: UserPreferences
    constraints: Optional[dict] = {}
