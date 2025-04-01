FROM python:3.10.12-slim

WORKDIR /bot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ../.env .env

CMD ["python", "bot_run.py"]