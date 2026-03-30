import psycopg2
from config import DB_CONFIG

def get_connection():
    """Establishes and returns a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def initialize_database():
    """Creates the necessary table(s) for the PhoneBook."""
    conn = get_connection()
    if not conn:
        return
    
    try:
        with conn.cursor() as cur:
            # Drop table if you need to reset during testing:
            # cur.execute("DROP TABLE IF EXISTS contacts;")
            
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(100) UNIQUE NOT NULL,
                    phone_number VARCHAR(20) NOT NULL
                );
            """)
            conn.commit()
            print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing table: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_database()