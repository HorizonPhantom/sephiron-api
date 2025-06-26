from fastapi import FastAPI, Request
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

app = FastAPI()

@app.post("/gpt")
async def gpt(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    if not prompt:
        return {"error": "Prompt ausente no corpo da requisição."}

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
