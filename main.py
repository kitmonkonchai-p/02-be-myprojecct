from fastapi import FastAPI,HTTPException
import pymongo
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
load_dotenv()
CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/check-db")
async def root():
    try:
        client = pymongo.MongoClient(CONNECTION_STRING)
        for prop, value in vars(client.options).items():
            print("Property: {}: Value: {} ".format(prop, value))
        return {"message": "connection ok"}
    
    except Exception :
        raise HTTPException(detail="Internal server error", status_code=400)