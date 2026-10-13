from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SecurityEvent(BaseModel):
    # 'title' is a required string. If someone sends an event without a title, it fails.
    title: str
    
    # 'severity' is a required string. We will expect things like "LOW", "HIGH", etc.
    severity: str
    
    # 'description' is a string, but the 'Optional' keyword means it's not strictly required.
    # We provide a default value of None if it's missing.
    description: Optional[str] = None
    
    # 'timestamp' must be a valid date-time. 
    # If the user doesn't provide one, it defaults to the exact time the event was received.
    timestamp: datetime = datetime.now()
