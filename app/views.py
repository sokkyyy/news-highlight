from flask import render_template
from app import app

# Home Page
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    sources = 'Hello, News Highlight'
    return render_template('index.html', sources=sources)

# Source News Articles
@app.route('/source/<source_id>')
def source(source_id):
    '''
    View source news articles page that returns the news articles of a source.
    '''
    # news_articles = "The news articles of a source"
    return render_template('source.html', news_articles=source_id)