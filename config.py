from pydantic import BaseSettings

class Settings(BaseSettings):
  API_URL: str

  class Config:
    env_file = './.env'

settings = Settings()  