from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import (
    get_gemini_api_key,
    get_gemini_model,
    get_model_provider,
)


def get_llm():
    return ChatGoogleGenerativeAI(
        model=get_gemini_model(),
        api_key=get_gemini_api_key()
    )
