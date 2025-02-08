from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_url = "http://localhost:8000"

settings = Settings()