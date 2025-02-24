from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница блога
@app.route('/blog')
def blog():
    posts = [
        {
            'title': 'Мой любимый кактус',
            'content': 'У меня дома живет очаровательный кактус. Он не требует особого ухода и радует глаз своей формой.',
            'author': 'Анна'
        },
        {
            'title': 'Пальма в моей гостиной',
            'content': 'Недавно я приобрела миниатюрную пальму. Она добавила уюта интерьеру и улучшила микроклимат.',
            'author': 'Иван'
        },
        {
            'title': 'Орхидея — королева цветов',
            'content': 'Орхидея стала настоящим украшением моего подоконника. Хотя за ней нужно следить, результат стоит усилий!',
            'author': 'Елена'
        }
    ]
    return render_template('blog.html', posts=posts)

# Страница контактов
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)