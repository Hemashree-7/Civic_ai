def analyze_complaint(description):

    text = description.lower()

    if "drainage" in text or "sewage" in text:
        return {
            "category": "Drainage Issue",
            "department": "Panchayat",
            "priority": "high"
        }

    elif "garbage" in text or "waste" in text:
        return {
            "category": "Garbage Issue",
            "department": "Municipal Corporation",
            "priority": "medium"
        }

    elif "flood" in text or "waterlogging" in text:
        return {
            "category": "Flood Emergency",
            "department": "Disaster Management",
            "priority": "critical"
        }

    elif "pothole" in text or "road damage" in text:
        return {
            "category": "Road Damage",
            "department": "PWD",
            "priority": "medium"
        }

    elif "medical" in text or "ambulance" in text:
        return {
            "category": "Medical Emergency",
            "department": "Health Department",
            "priority": "critical"
        }

    else:
        return {
            "category": "General Complaint",
            "department": "Municipal Office",
            "priority": "low"
        }