from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )
    database_url: str


Config = Settings(database_url="postgresql+asyncpg://nahidgabibov:password@localhost/test_db")