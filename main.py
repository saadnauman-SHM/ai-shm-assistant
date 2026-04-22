from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define request structure
class QuestionRequest(BaseModel):
    question: str

# Mock LLM function
def query(prompt):
    return {
        "generated_text": f"(Mock AI) Answer: {prompt}"
    }

@app.get("/")
def root():
    return {"message": "AI SHM Assistant running 🚀"}

# POST endpoint
@app.post("/ask")
def ask(request: QuestionRequest):
    result = query(request.question)
    return {"answer": result["generated_text"]}