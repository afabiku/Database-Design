class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///employee.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'  # Needed for forms and CSRF protection
