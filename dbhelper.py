import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'database.db')

class DBHelper:
    def __init__(self, db_path=DATABASE):
        self.db_path = db_path
    
    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable dictionary-like row access
        return conn
    
    def runQuery(self, query):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        except sqlite3.Error as e:
            print(f"[ERROR] runQuery failed: {e}")
        finally:
            conn.close()
    
    def getOneRow(self, query):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            return dict(row) if row else None  # Convert row to dictionary format
        except sqlite3.Error as e:
            print(f"[ERROR] getOneRow failed: {e}")
            return None
        finally:
            conn.close()
    
    def getRows(self, query):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]  # Convert rows to dictionary format
        except sqlite3.Error as e:
            print(f"[ERROR] getRows failed: {e}")
            return []
        finally:
            conn.close()

if __name__ == "__main__":
    db = DBHelper()
    db.runQuery("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL)")
