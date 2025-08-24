from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# Allow CORS for local frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB setup
MONGO_URI = "mongodb+srv://jsrihariseshbe24:xclkVC1buP9wpdGw@skillmate.v34gjcg.mongodb.net/skillmate?retryWrites=true&w=majority"  # Change to your Mongo URI
client = AsyncIOMotorClient(MONGO_URI)
db = client["SOC_FAIR"]
collection = db["registrations"]

@app.post("/submit")
async def submit_form(
    name: str = Form(..., alias="entry.490959701"),
    roll: str = Form(..., alias="entry.1973345164"),
    email: str = Form(..., alias="entry.1485161513"),
):
    doc = {"name": name, "roll": roll, "email": email}
    await collection.insert_one(doc)
    return {"message": "Form submitted successfully"}