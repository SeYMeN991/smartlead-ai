import os
from dotenv import load_dotenv 

load_dotenv()

BUSINESS_CONTEXT = os.getenv("BUSINESS_CONTEXT")
GROQ_API_KEY = os.getenv("groq_api_key")