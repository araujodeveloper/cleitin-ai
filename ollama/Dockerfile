FROM ollama/ollama

# Baixa o modelo ao iniciar a imagem
RUN ollama pull gemma:3b

EXPOSE 11434

CMD ["ollama", "serve"]
