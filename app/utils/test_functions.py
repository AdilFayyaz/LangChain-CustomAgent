import re
from datetime import datetime

def parse_event_details(input_str):
    # Initialize dictionary to store parsed details
    details = {}

    # Use regular expressions to extract each part
    details["location"] = re.search(r'"location":\s*"([a-zA-Z\s]+)"', input_str)
    details["capacity"] = re.search(r'"capacity":\s*(\d+)', input_str)
    details["date"] = re.search(r'"date":\s*"([\d\-]+)"', input_str)
    details["budget"] = re.search(r'"budget":\s*"?\$?(\d+)', input_str)
    details["cuisine"] = re.search(r'"cuisine":\s*"([a-zA-Z\s]+)"', input_str)
    details["entertainment"] = re.search(r'"entertainment":\s*"([a-zA-Z\s]+)"', input_str)
    
    # Return the extracted values, using default if not found
    result = {
        "location": details["location"].group(1) if details["location"] else "",
        "capacity": int(details["capacity"].group(1)) if details["capacity"] else 0,
        "date": datetime.strptime(details["date"].group(1), "%Y-%m-%d") if details["date"] else None,
        "cuisine": details["cuisine"].group(1) if details["cuisine"] else "",
        "entertainment": details["entertainment"].group(1) if details["entertainment"] else "",
        "budget": int(details["budget"].group(1)) if details["budget"] else 0
    }
    
    return result

# static locations
LOCATIONS = ["Los Angeles", "New York", "Chicago", "Miami", "San Francisco"]
def search_venues(event_details):
    event_details = parse_event_details(event_details)
    location = event_details.get("location", "")
    budget = event_details.get("budget", 0)
    
    if location not in LOCATIONS:
        return []
    
    results = [
        {"name": f"{location} Venue {chr(65+i)}", "price": (i+1)*20, "capacity": 50 + i*10, "location": location}
        for i in range(5)
        if (i+1)*20 <= budget
    ]
    return results

def find_caterers(event_details):
    event_details = parse_event_details(event_details)
    location = event_details.get("location", "")
    budget = event_details.get("budget", 0)
    if location not in LOCATIONS:
        return []
    
    cuisines = ["Italian", "Indian", "Chinese", "Mexican", "Mediterranean"]
    return [
        {"name": f"{location} Caterer {chr(65+i)}", "menu": cuisines[i], "price": (i+1)*15}
        for i in range(5)
        if (i+1)*15 <= budget
    ]

def suggest_entertainment(event_details):
    event_details = parse_event_details(event_details)
    budget = event_details.get("budget", 0)
    entertainment_types = ["DJ", "Magician", "Live Band", "Photobooth", "Karaoke"]
    return [
        {"name": f"{entertainment_types[i]} {chr(65+i)}", "price": (i+1)*10}
        for i in range(5)
        if (i+1)*10 <= budget
    ]