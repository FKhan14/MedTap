import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        print("Database connection established.")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    
if __name__ == "__main__":
    get_connection()