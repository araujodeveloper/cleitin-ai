#!/bin/bash

# Aguarda o Ollama estar disponível (caso precise em outro cenário)
echo "Iniciando container..."

# Faz o pull antes de iniciar o Ollama
echo "Fazendo o pull do modelo gemma3:1b..."
ollama pull gemma3:1b

# Inicia o servidor Ollama em primeiro plano (sem &)
echo "Iniciando o Ollama..."
exec ollama serve
