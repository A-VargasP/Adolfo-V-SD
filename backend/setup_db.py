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
            long_description TEXT NOT NULL,
            technologies TEXT NOT NULL,
            category TEXT NOT NULL,
            link TEXT,
            is_sample BOOLEAN DEFAULT 1
        )
    ''')
    
    # Insert sample projects
    samples = [
        (
            'EduCent', 
            'An educational management system designed to streamline learning and administrative tasks.', 
            'EduCent is a comprehensive management platform that centralizes the educational workflow. It provides intuitive tools for tracking student progress, managing schedules, and facilitating communication between instructors and learners. By reducing administrative overhead, EduCent empowers educators to focus on what matters most: teaching.',
            'React, Node.js, Express, PostgreSQL',
            'Software Development', 
            'https://github.com/A-VargasP/EduCent', 
            False
        ),
        (
            'FinTrack Pro', 
            'A robust financial tracking application for personal and small business accounting.', 
            'FinTrack Pro helps users visualize their cash flows through interactive dashboards and automated reporting. It categorizes expenses, tracks subscription payments, and generates detailed monthly financial summaries. The goal of this project was to simplify complex accounting tasks into an accessible, user-friendly interface.',
            'Vue.js, Django, SQLite, Chart.js',
            'Web Development', 
            'https://github.com/sample/fintrack', 
            False
        ),
        (
            'HealthSync App', 
            'A mobile health companion app that synchronizes data from wearables to provide insights.', 
            'HealthSync is designed to unify scattered health data from various fitness trackers and smartwatches. It aggregates metrics like heart rate, sleep cycles, and daily steps into a single unified profile. Using predictive algorithms, it offers personalized daily recommendations for optimal recovery and exercise.',
            'Flutter, Dart, Firebase, HealthKit API',
            'Mobile App', 
            'https://github.com/sample/healthsync', 
            False
        )
    ]
    
    conn.executemany('INSERT INTO projects (title, description, long_description, technologies, category, link, is_sample) VALUES (?, ?, ?, ?, ?, ?, ?)', samples)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_db()
    print("Database setup complete.")
