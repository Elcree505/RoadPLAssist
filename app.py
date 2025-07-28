from fastapi import FastAPI
from pydantic import BaseModel
from app.models.user import TravelRequest
from app.services.route_service import RouteService
from app.services.poi_service import POIService

app = FastAPI()

@app.post("/generate-itinerary")
async def generate_itinerary(request: TravelRequest):
    try:
        # Step 1: Get route information
        route_data = RouteService.get_directions(
            request.start_location, 
            request.end_location
        )
        
        # Step 2: Get POIs along the route
        pois = []
        for i in range(0, len(route_data['steps']), 2):
            location = route_data['steps'][i]['start_location']
            pois.extend(POIService.get_relevant_pois(
                f"{location['lat']},{location['lng']}", 
                request.preferences.interests
            ))

        # Step 3: Score and filter POIs
        scored_pois = []
        for poi in pois:
            score = POIService.score_poi(poi, request.preferences.interests)
            scored_pois.append({
                "poi": poi,
                "score": score
            })

        # Step 4: Optimize route with POIs
        # (This would integrate with OR-Tools service)

        return {
            "route": route_data,
            "recommended_pois": scored_pois[:settings.MAX_POIS]
        }
    except Exception as e:
        return {"error": str(e)}
