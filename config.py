class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://ksu:1234@db.achelsto.com:5432/employees?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = "dev"

config_by_name = {
    "dev": Config
}
