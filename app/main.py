from fastapi import FastAPI
from pydantic import BaseModel
import os
import random
import string
from pathlib import Path
from langchain_ollama import OllamaLLM
import chromadb

chroma_client = chromadb.Client()

OUTPUT_DIR = Path("respostas")
OUTPUT_DIR.mkdir(exist_ok=True)

OLLAMA_API = os.getenv("OLLAMA_API", "http://ollama:11434")
llm = OllamaLLM(model="gemma3:1b", base_url=OLLAMA_API)

collection = chroma_client.create_collection(name="my_collection")


app = FastAPI()

class Pergunta(BaseModel):
    prompt: str
    
    
def gerar_nome_arquivo():
    letras = string.ascii_lowercase + string.digits
    nome = ''.join(random.choices(letras, k=10))
    return OUTPUT_DIR / f"{nome}.txt"

@app.post("/perguntar")
def perguntar(pergunta: Pergunta):
    resposta = llm.invoke(pergunta.prompt)
    
    caminho_arquivo = gerar_nome_arquivo()
    
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(resposta)

    return {"resposta": resposta, "arquivo": str(caminho_arquivo)}
