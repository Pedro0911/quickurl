from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        original_url = request.form.get('url')
        code = generate_code()

        conn = get_db_connection()
        conn.execute('INSERT INTO urls (code, original_url) VALUES (?, ?)', (code, original_url))
        conn.commit()
        conn.close()

        short_url = request.host_url + code

    return render_template('index.html', short_url=short_url)

@app.route('/<code>')
def redirect_to_url(code):
    conn = get_db_connection()
    result = conn.execute('SELECT original_url FROM urls WHERE code = ?', (code,)).fetchone()
    conn.close()

    if result:
        return redirect(result['original_url'])
    return 'URL não encontrada.', 404

if __name__ == '__main__':
    app.run(debug=True)

