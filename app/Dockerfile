FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl bash

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]
