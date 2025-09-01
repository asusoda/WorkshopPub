from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="LeetCode to Production",
    description="A demo microservice that exposes LeetCode problems as APIs",
    version="1.0.0",
)


# Define request schema: 
# It’s how you define the shape of the data your API expects

# Valid Request:
# {
#   "nums": [2, 7, 11, 15],
#   "target": 9
# }

# 400 Bad Request:
# {
#   "nums": "not a list",
#   "target": "hello"
# }

class TwoSumRequest(BaseModel):
    nums: List[int]
    target: int



# Define response schema: 
# It defines the shape of the data your API will return

# Example when a solution exists:

# {
#   "result":
#   "error":
# } 

class TwoSumResponse(BaseModel):
    result: Optional[List[int]] = None
    error: Optional[str] = None


# FastAPI route handler / endpoint function

@app.post("/two_sum", response_model=TwoSumResponse)
# Whenever someone sends a POST request to the path /two_sum, run the function below

def two_sum(req: TwoSumRequest):
    """Solve the Two Sum problem as an API endpoint"""

    # Add your LeetCode Logic in here!
    seen = {}  # value → index
        
    for i, num in enumerate(req.nums):
        complement = req.target - num
        if complement in seen:
            return {'result' : [seen[complement], i]}
        seen[num] = i
    # return {"error": "No two sum solution found"}