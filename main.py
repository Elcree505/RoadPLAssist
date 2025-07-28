from flask import Flask, request, jsonify
from dotenv import load_dotenv
from config import settings
from user import TravelRequest
from route_service import RouteService
from poi_service import POIService
import os

app = Flask(__name__)
MAX_POIS = int(os.getenv("MAX_POIS", 10))

@app.route("/generate-itinerary", methods=["POST"])
def generate_itinerary():
    try:
        # Parse and validate input
        data = request.get_json()
        travel_request = TravelRequest(**data)

        # Step 1: Get route information
        route_data = RouteService.get_directions(
            travel_request.start_location, 
            travel_request.end_location
        )

        # Step 2: Get POIs along the route
        pois = []
        for i in range(0, len(route_data['steps']), 2):
            location = route_data['steps'][i]['start_location']
            pois.extend(POIService.get_relevant_pois(
                f"{location['lat']},{location['lng']}", 
                travel_request.preferences.interests
            ))

        # Step 3: Score and filter POIs
        scored_pois = []
        for poi in pois:
            score = POIService.score_poi(poi, travel_request.preferences.interests)
            scored_pois.append({
                "poi": poi,
                "score": score
            })

        # Step 4: Return route + top POIs
        return {
            "route": route_data,
            "recommended_pois": sorted(scored_pois, key=lambda x: x["score"], reverse=True)[:MAX_POIS]
        }
    except Exception as e:
        return {"error": str(e)}, 500
