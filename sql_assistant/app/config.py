import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

def get_db_path():
    return Path(__file__).resolve().parent.parent / "data" / "sales_demo.db"

def get_model_provider():
    return os.getenv('MODEL_PROVIDER','gemini').lower()


def get_gemini_api_key():
    api_key=os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError('API Key not found')
    return api_key

def get_gemini_model():
    return os.getenv('GEMINI_MODEL','gemini-3.6-flash')
