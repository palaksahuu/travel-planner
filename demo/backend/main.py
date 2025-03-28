from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import openai

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Fetch API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX_ID = os.getenv("GOOGLE_CX_ID")
TRIPADVISOR_API_KEY = os.getenv("TRIPADVISOR_API_KEY")

# ✅ Validate API keys
if not OPENAI_API_KEY:
    raise RuntimeError("⚠️ Missing OPENAI_API_KEY. Set it as an environment variable.")
if not GOOGLE_API_KEY:
    raise RuntimeError("⚠️ Missing GOOGLE_API_KEY. Set it as an environment variable.")
if not GOOGLE_CX_ID:
    raise RuntimeError("⚠️ Missing GOOGLE_CX_ID. Set it as an environment variable.")
if not TRIPADVISOR_API_KEY:
    raise RuntimeError("⚠️ Missing TRIPADVISOR_API_KEY. Set it as an environment variable.")

# ✅ Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# ✅ Create FastAPI app
app = FastAPI()

# 📝 Test Route
@app.get("/")
def home():
    return {"message": "Welcome to the AI Travel Assistant!"}

# 🎯 Generate Travel Itinerary
@app.post("/generate-itinerary/")
async def generate_itinerary(request_data: dict):
    try:
        destination = request_data.get("destination")
        budget = request_data.get("budget")
        travel_style = request_data.get("travel_style")

        if not destination or not budget or not travel_style:
            raise HTTPException(status_code=400, detail="Missing required fields!")

        # ✅ Prompt for OpenAI API
        prompt = f"Generate a detailed {budget} travel itinerary for {destination} focusing on {travel_style} experiences."

        # 🔥 Call OpenAI API (Updated Version)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert travel planner."},
                {"role": "user", "content": prompt},
            ],
        )

        # ✅ Return the generated plan
        generated_itinerary = response.choices[0].message.content
        return {"itinerary": generated_itinerary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
