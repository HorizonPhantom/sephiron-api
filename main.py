from fastapi import FastAPI, Request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/gpt")
async def gpt(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return {"response": response["choices"][0]["message"]["content"]}