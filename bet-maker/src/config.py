from pydantic import Field
from pydantic_settings import BaseSettings

class DBConfig(BaseSettings):
    DB_USER: str = Field(...)
    DB_PASSWORD: str = Field(...)
    DB_HOST: str = Field(...)
    DB_PORT: int = Field(...)
    DB_NAME: str = Field(...)

    @property
    def async_database_postgres(self) -> str:
        """Формирует асинхронный URL для подключения к PostgreSQL."""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def alembic_database_postgres(self) -> str:
        """Формирует асинхронный URL для подключения к PostgreSQL."""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@localhost:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_prefix = "BET_"

class HttpSettings(BaseSettings):
    URL_GET_ACTIVE_EVENTS: str


http_config = HttpSettings()
db_config = DBConfig()
