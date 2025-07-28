from pydantic import BaseModel
from typing import List, Dict, Optional

class POI(BaseModel):
    name: str
    latitude: float
    longitude: float
    address: Optional[str]
    category: Optional[str]
    rating: Optional[float]
    score: Optional[float]  # optional custom score

class RouteSegment(BaseModel):
    start_address: str
    end_address: str
    duration_text: str
    distance_text: str

class ItineraryResponse(BaseModel):
    route: List[RouteSegment]
    pois: List[POI]
    total_duration_minutes: Optional[int]
    notes: Optional[str] = None
