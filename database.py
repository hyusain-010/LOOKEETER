import sqlite3

DATABASE = "database.db"

def init_db():
    try:
        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            search_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()

    except sqlite3.Error as e:
        print(f"Database Error: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")