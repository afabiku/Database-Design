import sqlite3

# === File paths ===
CREATE_DB_SQL = 'create_employee_db.sql'
DUMMY_DATA_SQL = 'populate_tables.sql'

# === Read SQL file content ===
def load_sql_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content.split(';')  # split by semicolon

# === Execute SQL statements ===
def execute_sql_file(cursor, sql_statements):
    for statement in sql_statements:
        stmt = statement.strip()
        if stmt:
            try:
                cursor.execute(stmt)
            except sqlite3.Error as err:
                print(f"[!] Error: {err}")
                print(f" -> Statement: {stmt}")

def main():
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()

        print("[+] Running schema creation script...")
        create_statements = load_sql_file(CREATE_DB_SQL)
        execute_sql_file(cursor, create_statements)

        print("[+] Running dummy data script...")
        dummy_statements = load_sql_file(DUMMY_DATA_SQL)
        execute_sql_file(cursor, dummy_statements)

        conn.commit()
        cursor.close()
        conn.close()
        print("[✓] Database initialized successfully.")

    except sqlite3.Error as err:
        print(f"[!] SQLite error: {err}")

if __name__ == '__main__':
    main()
