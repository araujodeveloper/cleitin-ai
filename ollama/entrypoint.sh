#!/bin/bash

# Inicia o servidor Ollama em background
ollama serve &

# Aguarda o Ollama estar disponível
echo "Aguardando o Ollama iniciar..."
until curl --silent http://localhost:11434 > /dev/null; do
  sleep 1
done

# Faz o pull do modelo
echo "Fazendo o pull do modelo gemma3:1b..."
ollama pull gemma3:1b

# Aguarda o processo original (ollama serve) para manter o container ativo
wait
