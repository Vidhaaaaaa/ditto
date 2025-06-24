from fastapi import FastAPI

import os
from dotenv import load_dotenv

import requests

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")


def insert_text(text):
    url = f"{SUPABASE_URL}/rest/v1/sshot_text"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    payload = {
        "text": text  # make sure your table has a column called 'text'
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Status:", response.status_code)
    print("Response:", response.text)
