from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()

class DBConfig(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

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
