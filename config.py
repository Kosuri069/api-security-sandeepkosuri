# config.py
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("Missing API key. Set OPENWEATHER_API_KEY in .env")
