
class Config():
    SECRET_KEY= "bp54aRKlRj0p8VL£"

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = 'flask'

config = {'development': DevelopmentConfig}