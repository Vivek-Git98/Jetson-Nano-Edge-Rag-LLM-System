from fastapi import FastAPI
from pydantic import BaseModel

from rag_engine import ask_query

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Planet AI LLM API Running"}

@app.post("/ask")
def ask(data: QueryRequest):

    response = ask_query(data.question)

    return {
        "question": data.question,
        "answer": response
    }