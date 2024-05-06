from flask import Flask, render_template

def create_app():
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
    ]

    @app.route('/')
    def index():
        return render_template('index.html', news_articles=news_articles)

    return app

app = create_app()

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
