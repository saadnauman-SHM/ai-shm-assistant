from fastapi import APIRouter, HTTPException
from app.schemas.request import QuestionRequest
from app.services.llm_service import query

router = APIRouter()

@router.post("/ask")
def ask(request: QuestionRequest):
    try:
        result = query(request.question)

        return {
            "status": "success",
            "data": {
                "answer": result["generated_text"],
                "source": "mock_llm"
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))