from flask import render_template,request,redirect,url_for
from app import app
from .requests import get_sources,get_source_articles,get_article

# Home Page
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    title = 'Home - Welcome to News Highlight'
    sources = get_sources()

    search_source = request.args.get('search')

    if search_source:
        return redirect(url_for('search',source_id=search_source))
    else:
        return render_template('index.html',title=title ,sources=sources)

# Source News Articles
@app.route('/source/<source_id>')
def source(source_id):
    '''
    View source news articles function that returns the news articles of a source.
    '''
    news_articles = get_source_articles(source_id)
    title = f'{source_id}'
    return render_template('source.html', title=title, news_articles=news_articles)

# Read News Article
@app.route('/content/<source_id>/<article_title>')
def content(source_id, article_title):
    '''
    View content function that returns the news content of a source's news article.
    '''
    
    article = get_article(source_id,article_title)
    title = f'{article.title}.'
    return render_template('content.html', title=title, article=article)

# Search for source
@app.route('/search/<source_id>')
def search(source_id):
    '''
    '''
    search_results = get_source_articles(source_id)
    title = f'Search results for {source_id}'
    return render_template('search.html', title=title, search=search_results)