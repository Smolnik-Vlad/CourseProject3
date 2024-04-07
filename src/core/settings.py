from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    NEO4J_PATH: str
    NEO4J_PASSWORD: str
    NEO4J_USER: str

    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str


settings = Settings()
