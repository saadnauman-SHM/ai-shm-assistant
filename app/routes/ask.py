from fastapi import APIRouter
from app.schemas.request import QuestionRequest
from app.services.llm_service import query

router = APIRouter()   # 👈 THIS LINE IS CRITICAL

@router.post("/ask")
def ask(request: QuestionRequest):
    result = query(request.question)
    return {"answer": result["generated_text"]}