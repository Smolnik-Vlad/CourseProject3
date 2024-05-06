FROM python:3.10.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Install dependencies
COPY requirements.txt .
COPY ../scripts/entrypoint.sh .


RUN chmod +x ./entrypoint.sh


RUN pip3 install -r requirements.txt
COPY . /code