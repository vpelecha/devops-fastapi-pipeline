from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DevOps uv Pipeline")

class SumRequest(BaseModel):
    a: int
    b: int

class SumResponse(BaseModel):
    result: int

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

@app.post("/sum", response_model=SumResponse)
def sum_numbers(payload: SumRequest) -> SumResponse:
    return SumResponse(result=payload.a + payload.b)
