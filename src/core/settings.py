from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str
    database_user: str
    database_password: str
    database_name: str


settings = Settings()
