from dotenv import load_dotenv
import os

# Load .env
load_dotenv(dotenv_path=".env")

class Settings:
    APP_NAME: str = "AI SHM Assistant"
    APP_VERSION: str = "1.0.0"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")  # ✅ CORRECT

settings = Settings()

print("DEBUG API KEY:", settings.OPENAI_API_KEY)