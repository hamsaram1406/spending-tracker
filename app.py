from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import json
from datetime import datetime

app = Flask(__name__)

# Database setup
DB_PATH = 'spending.db'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS spending
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  amount REAL NOT NULL,
                  category TEXT NOT NULL,
                  date TEXT NOT NULL,
                  notes TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/entries', methods=['GET'])
def get_entries():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT id, amount, category, date, notes FROM spending ORDER BY date DESC')
    rows = c.fetchall()
    conn.close()
    
    entries = []
    for row in rows:
        entries.append({
            'id': row['id'],
            'amount': row['amount'],
            'category': row['category'],
            'date': row['date'],
            'notes': row['notes']
        })
    return jsonify(entries)

@app.route('/api/entries', methods=['POST'])
def add_entry():
    data = request.get_json()
    
    conn = get_db()
    c = conn.cursor()
    c.execute('INSERT INTO spending (amount, category, date, notes) VALUES (?, ?, ?, ?)',
              (float(data['amount']), data['category'], data['date'], data.get('notes', '')))
    conn.commit()
    entry_id = c.lastrowid
    conn.close()
    
    return jsonify({
        'id': entry_id,
        'amount': float(data['amount']),
        'category': data['category'],
        'date': data['date'],
        'notes': data.get('notes', '')
    }), 201

@app.route('/api/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM spending WHERE id = ?', (entry_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True}), 200

@app.route('/api/entries/clear-all', methods=['DELETE'])
def clear_all():
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM spending')
    conn.commit()
    conn.close()
    
    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True)
