# from pydantic import BaseSettings
#
# class Settings(BaseSettings):
#     database_url: str
#     secret_key: str
#     debug: bool = False
#
#     class Config:
#         env_file = ".env"

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )
    database_url: str


Config = Settings(database_url="postgresql+asyncpg://nahidgabibov:password@localhost/test_db")