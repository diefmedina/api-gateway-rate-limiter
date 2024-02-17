import os

# Load environment variables from .env
from dotenv import load_dotenv

load_dotenv()

# Rate limiter configuration
REQUESTS_PER_MINUTE = int(os.getenv("REQUESTS_PER_MINUTE", 100))
# Add more configuration options as needed