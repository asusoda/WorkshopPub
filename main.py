from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="LeetCode to Production",
    description="A demo microservice that exposes LeetCode problems as APIs",
    version="1.0.0",
)

# Define request schema
class TwoSumRequest(BaseModel):
    nums: List[int]
    target: int

# Define response schema
class TwoSumResponse(BaseModel):
    result: Optional[List[int]] = None
    error: Optional[str] = None

@app.post("/two_sum", response_model=TwoSumResponse)
def two_sum(req: TwoSumRequest):
    """Solve the Two Sum problem as an API endpoint"""
    indices = {}
    for i, num in enumerate(req.nums):
        complement = req.target - num
        if complement in indices:
            return {"result": [indices[complement], i]}
        indices[num] = i
    return {"error": "No two sum solution found"}
