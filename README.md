# Two Sum API

This project turns the classic "Two Sum" LeetCode problem into a deployable microservice using Flask. It serves as an educational example for solving algorithmic problems, exposing them via a REST API, and deploying them to a production-ready environment (e.g., Replit, Vercel).

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use the same element twice.

## Example

**Input:**
```json
{
  "nums": [2, 7, 11, 15],
  "target": 9
}
```

**Output:**
```json
{
  "indices": [0, 1]
}
```

## API Endpoint

### `POST /api/two-sum`

**Request Body:**
```json
{
  "nums": [int, int, ...],
  "target": int
}
```

**Response:**
```json
{
  "indices": [int, int]
}
```

**Error Response:**
```json
{
  "error": "Invalid input"
}
```

## Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

## Deployment

This app can be deployed to:
- Replit
- Vercel (using Flask + ASGI wrapper like `asgiref`)
- Render or Railway

Make sure to expose the `/api/two-sum` route and test it with tools like `curl` or Postman.

Deployment on Replit & Testing via PowerShell
To deploy this microservice on Replit, simply create a new Python Repl, paste the contents of main.py (Flask app), and click Run. Replit will host your app at a temporary public URL (e.g., https://<random-id>.replit.dev/).

To test the /two_sum endpoint using PowerShell, use the following command:

Invoke-RestMethod `
  -Method POST `
  -Uri "https://<your-replit-url>/two_sum" `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"nums":[2,7,11,15],"target":18}'
This will return the indices of the two numbers that sum to the target in JSON format (e.g., [1,2]). Make sure to replace the URL with your actual Replit endpoint.


## Project Structure

```
two_sum_api/
├── app.py
├── requirements.txt
├── README.md
└── venv/ (virtual environment)
```

## License

This project is provided for educational purposes and does not carry any official license. You may adapt and extend it for teaching, demo, or personal use.
