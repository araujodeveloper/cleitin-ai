from fastapi import FastAPI
from pydantic import BaseModel
import os
from langchain_ollama import OllamaLLM

OLLAMA_API = os.getenv("OLLAMA_API", "http://ollama:11434")
llm = OllamaLLM(model="gemma3:1b", base_url=OLLAMA_API)

app = FastAPI()

class Pergunta(BaseModel):
    prompt: str

@app.post("/perguntar")
def perguntar(pergunta: Pergunta):
    resposta = llm.invoke(pergunta.prompt)
    return {"resposta": resposta}
