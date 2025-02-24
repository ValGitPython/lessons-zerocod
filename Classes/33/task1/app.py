from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Форматирование даты и времени
    return f"<h1>Текущая дата и время:</h1><p>{current_time}</p>"

if __name__ == '__main__':
    app.run(debug=True)