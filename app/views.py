from flask import render_template
from app import app
from .requests import get_sources,get_source_articles

# Home Page
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    title = 'Home - Welcome to News Highlight'
    sources = get_sources()
    return render_template('index.html',title=title ,sources=sources)

# Source News Articles
@app.route('/source/<source_id>')
def source(source_id):
    '''
    View source news articles page that returns the news articles of a source.
    '''
    news_articles = get_source_articles(source_id)
    title = f'{source_id}'
    return render_template('source.html', title=title, news_articles=news_articles)

# Content of News Article
@app.route('/')