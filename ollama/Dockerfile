FROM ollama/ollama

RUN apt-get update && apt-get install -y curl bash

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 11434

ENTRYPOINT ["/entrypoint.sh"]
