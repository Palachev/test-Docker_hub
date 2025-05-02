from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Привет от Flask!"

@app.route('/db')
def test_db():
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return f"База данных работает: {result}"
    except Exception as e:
        return f"Ошибка подключения к БД: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)