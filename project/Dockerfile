FROM python:3.13.3-slim-bookworm

WORKDIR /usr/src/app

# Prevent Python from writing .pyc files (compiled bytecode)
# This reduces container size and avoids potential permission issues
ENV PYTHONDONTWRITEBYTECODE 1

# Force Python to run in unbuffered mode
# This ensures that Python output is sent straight to terminal without being buffered
# Important for Docker containers to see logs in real-time
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .