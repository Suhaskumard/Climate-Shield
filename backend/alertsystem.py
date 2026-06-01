import requests
from flask import jsonify

def fetch_gis_alert_data():
    """
    Fetches external GIS climate alerts data source.
    Implements mandatory error handling to return standard HTTP status codes.
    """
    GIS_API_URL = "https://external-gis-source.com" 
    
    try:
        # Added a 5-second timeout parameter to prevent backend hangs
        response = requests.get(GIS_API_URL, timeout=5)
        
        # Triggers an HTTP error if the remote server answers with a 4xx or 5xx code
        response.raise_for_status() 
        
        # Safely parsing JSON formatting data payload
        return response.json(), 200

    except requests.exceptions.Timeout:
        # Handles Case: Gateway Timeout (504)
        return jsonify({"error": "External GIS service timed out. Please try again."}), 504

    except (requests.exceptions.RequestException, ValueError):
        # Handles Case: Offline status, connection drops, or malformed HTML response data formatting (503)
        return jsonify({"error": "External GIS service is unavailable or returned an invalid response."}), 503
 
