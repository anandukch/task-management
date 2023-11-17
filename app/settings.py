from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str

    class Config:
        env_file = "./.env"
        case_sensitive = True


settings = Settings()
