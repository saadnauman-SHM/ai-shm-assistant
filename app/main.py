from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.ask import router as ask_router
from app.core.config import settings

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME
)

# ✅ Add CORS middleware (fixes Swagger "Failed to fetch")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (safe for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} running 🚀"}

# Include routes
app.include_router(ask_router)