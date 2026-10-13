from fastapi import FastAPI
from app.schemas.security_event import SecurityEvent # <-- 1. Import our new model

# Create the main application instance
app = FastAPI(title="AegisTrace API")

# Day 1: Health Check Endpoint
@app.get("/")
def health_check():
    return {
        "status": "ok", 
        "message": "AegisTrace Backend is running!"
    }

# Day 2: New POST Endpoint for Events
@app.post("/api/v1/events")
def create_event(event: SecurityEvent): # <-- 2. Tell FastAPI to expect this model
    # If the code reaches this point, the data is 100% valid!
    
    # In a real app, we would save 'event' to a database here.
    # For today, we are just returning it back to prove it worked.
    return {
        "status": "success",
        "message": "Security event received and validated!",
        "data": event
    }
