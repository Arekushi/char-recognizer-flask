class Config:
    DEBUG = False
    PORT = 5000


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    DEVELOPMENT = True
    CONFIG_NAME = 'development'


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    CONFIG_NAME = 'production'


configs = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    default=DevelopmentConfig
)
