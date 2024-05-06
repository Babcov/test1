from flask import Flask, render_template

app = Flask(__name__)

news_articles = [
    {
        'title': 'Новость 1',
        'content': 'Содержание новости 1'
    },
    {
        'title': 'Новость 2',
        'content': 'Содержание новости 2'
    },
    # Добавьте больше новостей
]

# Главная страница
@app.route('/')
def index():
    return render_template('index.html', news_articles=news_articles)

if __name__ == '__main__':
    app.run(debug=True)
