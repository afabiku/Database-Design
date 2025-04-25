1. **Create a virtual environment** (recommended)

   On **Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   On **Mac/Linux**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```


2. **Install all dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *(If `requirements.txt` does not exist, you can install manually:)*

   ```bash
   pip install flask flask_sqlalchemy psycopg2-binary flask_wtf
   ```


3. **Set the FLASK_APP environment variable**

   On **Windows**:
   ```bash
   $env:FLASK_APP = "app.py"
   ```

   On **Mac/Linux**:
   ```bash
   export FLASK_APP=app.py
   ```


4. **Run the Flask app**

   ```bash
   flask run
   ```


5. **Open your browser**

   Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

