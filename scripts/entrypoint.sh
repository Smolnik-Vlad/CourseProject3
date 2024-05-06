#!/bin/sh

uvicorn src.main:app --host ${APP_HOST:-"0.0.0.0"} --port ${APP_PORT:-8080} --reload

exec "$@"