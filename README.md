# LeetCode to Production (Workshop Demo)

This project demonstrates how to turn a LeetCode problem into a production-ready microservice using **FastAPI**.

---

## Run Locally

1. Clone the repository and navigate to the project directory.

2. Install dependencies:
   `pip install -r requirements.txt`

3. Start the server:
   `uvicorn main:app --reload`

4. Open http://127.0.0.1:8000/docs to test with Swagger UI.

---

## Example Request

Endpoint:  

`POST /two_sum`

Request Body:
```
{
  "nums": [2, 7, 11, 15],
  "target": 9
}
```

Response:
```
{
  "result": [0, 1]
}
```

API ENDPOINT:
The function returning the result!
If no solution exists:
{
  "error": "No two sum solution found"
}

---

## Deploying on Vercel

1. Push this repo to GitHub.  
2. Go to https://vercel.com, click New Project, and import your repo.  
3. Set the Framework Preset = Python.  
4. Add a vercel.json file to the root of the repo:
   {
     "builds": [
       { "src": "main.py", "use": "@vercel/python" }
     ],
     "routes": [
       { "src": "/(.*)", "dest": "main.py" }
     ]
   }
5. Deploy → test at:  
   https://`<`your-vercel-app`>`.vercel.app/two_sum

---

## Learning Outcomes

- Turn a LeetCode problem into a backend microservice.  
- Learn to design APIs using **FastAPI** + **Pydantic**.  
- Generate interactive docs with **Swagger UI**.  
- Deploy a production-ready service using **Vercel**.  

---

## Future Improvements

- Add authentication via tokens.  
- Deploy with Docker + Kubernetes.  
- Expand beyond *Two Sum* → more LeetCode problems.  
- Use as a **resume project** on GitHub + LinkedIn.  
# WorkshopPub
