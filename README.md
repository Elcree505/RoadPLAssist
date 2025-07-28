# 🗺️ RoadPlanAssist

**RoadPlanAssist** is an AI-powered travel planning tool that generates optimized travel itineraries. It calculates driving routes, recommends relevant points of interest (POIs) along the way, scores them based on user preferences, and integrates weather data for better travel decisions.

---

## 🚀 Features

- 🚘 Route planning with Google Maps API
- 🧭 POI discovery and recommendation via Google Places
- 🔍 Custom scoring of POIs based on user interests
- 🧠 Route optimization using Google OR-Tools
- ☀️ Weather forecasting with OpenWeatherMap (or Tomorrow.io)
- 🔧 Configurable preferences (interests, budget, dietary restrictions, etc.)

---

## 🛠️ Technology Stack

| Category          | Tool/Library           |
|------------------|------------------------|
| Programming      | Python 3.11            |
| Web Framework    | Flask                  |
| API Integration  | Google Maps, Places API, OpenWeatherMap |
| Data Modeling    | Pydantic               |
| Settings Mgmt    | Hardcoded in `config.py` (dev-only) |
| Geolocation      | geopy                  |
| Optimization     | Google OR-Tools        |
| HTTP Requests    | requests               |

---

## 📁 Project Structure

