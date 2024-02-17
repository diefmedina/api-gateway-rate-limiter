import os

from dotenv import load_dotenv

load_dotenv()

REQUESTS_PER_MINUTE = int(os.getenv("REQUESTS_PER_MINUTE", 100))
