from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    """Настройки базы данных"""
    HOST: str
    PORT: int = 5432
    USERNAME: str
    PASSWORD: str
    DATABASES: str

    class Config:
        env_prefix = 'DB_'
        case_sensitive = False


databases_settings = DatabaseSettings()


database_url = (f'postgresql+asyncpg://{databases_settings.USERNAME}:{databases_settings.PASSWORD}'
                f'@{databases_settings.HOST}:{databases_settings.PORT}/{databases_settings.DATABASES}')


class RedisSettings(BaseSettings):
    """Настройки Redis."""
    HOST: str
    PORT: int = 6379

    class Config:
        env_prefix = 'BROKER_'
        case_sensitive = False
    
    @property
    def url(self):
        return f'redis://{self.HOST}:{self.PORT}/0'


redis_settings = RedisSettings()