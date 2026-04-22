import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = "AI SHM Assistant"
    ENV: str = os.getenv("ENV", "development")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

settings = Settings()