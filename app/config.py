class Config:
    '''
    General configuration parent class.
    '''
    SOURCES_API_BASE_URL= 'https://newsapi.org/v2/sources?apiKey={}'
    SOURCE_ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    
class ProdConfig(Config):
    '''
    Production configuration child class.

    Args:
        Config: The parent configuration class with General configuration setting
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class.

    Args:
        Config: The parent configuration class with General configuration setting
    '''
    DEBUG = True
