class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://ksu:1234@db.achelsto.com:5432/employees?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
