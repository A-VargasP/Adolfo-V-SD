import sqlite3
import os

DB_PATH = 'portfolio.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def setup_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            link TEXT,
            is_sample BOOLEAN DEFAULT 1
        )
    ''')
    
    # Insert sample projects
    samples = [
        ('EduCent', 'An educational management system designed to streamline learning and administrative tasks.', 'Software Development', 'https://github.com/A-VargasP/EduCent', False),
        ('FinTrack Pro', 'A robust financial tracking application for personal and small business accounting. Built with React and Node.js.', 'Web Development', 'https://github.com/sample/fintrack', False),
        ('HealthSync App', 'A mobile health companion app that synchronizes data from wearables to provide insights. Built with Flutter.', 'Mobile App', 'https://github.com/sample/healthsync', False)
    ]
    
    conn.executemany('INSERT INTO projects (title, description, category, link, is_sample) VALUES (?, ?, ?, ?, ?)', samples)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_db()
    print("Database setup complete.")
