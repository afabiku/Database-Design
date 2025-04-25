class Config:
    SQLALCHEMY_DATABASE_URI = 'database connection'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = "dev"

config_by_name = {
    "dev": Config
}
