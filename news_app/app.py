import sys
print(sys.path)
from flask import Flask, render_template

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

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
