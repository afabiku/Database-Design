# Employee Manager

A Flask-based web app to manage employee data, PTO requests, and scheduling for internal company use.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### 2. Set Up Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the App

```bash
python run.py
```

Then open your browser and go to:  
**http://localhost:8080**

---

## Database

To set up the database schema, run the SQL file in `/sql/tables.sql` using any MySQL-compatible database.

---

## Project Structure

```
app/
├── routes/          # Flask Blueprints
├── static/          # CSS files
└── templates/       # HTML templates

sql/
└── tables.sql       # Schema for MySQL

config.py            # App configuration  
run.py               # Entry point for the app  
requirements.txt     # Python dependencies
```

---

## Notes

- Configuration settings are in `config.py`
- HTML templates are in `app/templates/`
- Styling is in `app/static/style.css`
