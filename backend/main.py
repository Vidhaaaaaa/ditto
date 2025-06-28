from fastapi import FastAPI

import os
from dotenv import load_dotenv

import requests

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "yes this works"}
