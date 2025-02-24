import os
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # Redis Configuration
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

    # JWT Authentication
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key")  # Change in production
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600))  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", 86400))  # 1 day

    # Flask Caching (Uses Redis)
    CACHE_TYPE = "redis"
    CACHE_REDIS_HOST = REDIS_HOST
    CACHE_REDIS_PORT = REDIS_PORT
    CACHE_REDIS_DB = REDIS_DB
    CACHE_REDIS_PASSWORD = REDIS_PASSWORD

    # Flask-Limiter (Rate Limiting)
    RATELIMIT_STORAGE_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}" if REDIS_PASSWORD else f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    RATELIMIT_DEFAULT = "100 per minute"
    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'


class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}