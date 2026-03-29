"""
AI Translation Agent - 智能翻译服务
特色:保留语气和文化特色的高质量翻译
"""
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Translation Agent")
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)

class TranslationRequest(BaseModel):
    text: str
    target_language: str
    source_language: str = "auto"
    preserve_tone: bool = True

class TranslationResponse(BaseModel):
    translated_text: str
    source_language: str
    target_language: str
    character_count: int
    cost: float

@app.get("/")
async def root():
    return {
        "service": "AI Translation Agent",
        "version": "1.0.0",
        "features": ["Auto language detection", "Tone preservation", "20+ languages"]
    }

@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    """翻译文本，保留语气和文化特色"""
    try:
        # 构建提示词
        prompt = f"""Translate the following text to {request.target_language}.
        
IMPORTANT RULES:
- Preserve the original tone and style
- Keep cultural nuances when possible
- Maintain formatting
- If source language is 'auto', detect it automatically

Text to translate:
{request.text}

Respond with ONLY the translated text, nothing else."""

        # 调用GPT API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        translated = response.choices[0].message.content.strip()
        char_count = len(request.text)
        cost = (char_count / 100) * float(os.getenv("PRICE_PER_100_CHARS", 0.01))
        
        return TranslationResponse(
            translated_text=translated,
            source_language=request.source_language,
            target_language=request.target_language,
            character_count=char_count,
            cost=cost
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
