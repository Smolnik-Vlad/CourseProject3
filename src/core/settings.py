from typing import Optional

from pydantic.v1 import BaseSettings


class S3Settings(BaseSettings):
    MINIO_ACCESS_KEY: str = '7oCarxewWkDoXGJ7uYES'
    MINIO_SECRET_KEY: str = 'zENVKI5tWsgqbX3u7FWO1Q1F3gap0pIEWcLVVPHR'
    BUCKET_NAME: str = 'art'
    ENDPOINT_URL: str = 'http://minio:9000'
    EXTERNAL_URL: str = 'http://localhost:9000'


class Settings(BaseSettings):
    NEO4J_PATH: str
    NEO4J_PASSWORD: str
    NEO4J_USER: str

    s3: S3Settings = S3Settings()


settings = Settings()
