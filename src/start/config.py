from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
