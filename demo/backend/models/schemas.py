from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import date
from enum import Enum

# ✅ Define Allowed Budget Options using Enum
class Budget(str, Enum):
    budget = "budget"
    moderate = "moderate"
    luxury = "luxury"

# ✅ Define Allowed Travel Styles using Enum
class TravelStyle(str, Enum):
    adventure = "adventure"
    relaxation = "relaxation"
    cultural = "cultural"
    foodie = "foodie"

# ✅ Corrected TravelRequest Model
class TravelRequest(BaseModel):
    destination: str
    starting_location: str
    trip_duration: int
    budget: Budget
    start_date: date  # 📅 Correctly typed as date
    end_date: date  # 📅 Correctly typed as date
    travel_style: List[TravelStyle]
    preferences: Optional[str] = None

    # ✅ Pydantic v2.x Config to Allow Arbitrary Types
    model_config = ConfigDict(arbitrary_types_allowed=True)
