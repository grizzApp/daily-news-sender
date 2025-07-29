import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY: str = os.getenv('NEWS_API_KEY')
NEWS_API_ENDPOINT: str = os.getenv('NEWS_API_ENDPOINT')
EMAIL_ADDRESS: str = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD: str = os.getenv('EMAIL_PASSWORD')
RECIPIENT: str = os.getenv('RECIPIENT')