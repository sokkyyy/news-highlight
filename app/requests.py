from app import app
import urllib.request,json
from .models import source,news_article

Source = source.Source
Article = news_article.News_Article

# Getting API key
sources_api_key = app.config['NEW_API_KEY']

# Getting the sources base url
sources_url = app.config['SOURCES_API_BASE_URL']
source_articles_url = app.config['SOURCE_ARTICLES_BASE_URL']

def get_sources():
    '''
    Function that will get the json response to our sources request.
    '''
    get_sources_url = sources_url.format(sources_api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)
        
    return source_results

def process_source_results(source_list):
    '''
    Function that processes the source results and tranforms them to a list of objects
    
    Args:
        source_list: A list of sources in dictionary format that contains source details. 
    Returns:
        source_results: A list of source dictionaries.
    '''

    source_results= []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        if id:
            source_object = Source(id,name,description)
            source_results.append(source_object)
    
    return source_results

def get_source_articles(id):
    '''
    Function to request to get the json response of source news articles.
    '''
    get_source_articles_url = source_articles_url.format(id,sources_api_key)

    with urllib.request.urlopen(get_source_articles_url) as url:
        source_articles_data = url.read()
        source_articles_response = json.loads(source_articles_data)

        article_results = None

        if source_articles_response['articles']:
            source_articles_list = source_articles_response['articles']
            article_results = process_articles_results(source_articles_list)
    
    return article_results

def process_articles_results(articles_list):
    '''
    Function that processes the articles results and tranforms them to a list of objects
    
    Args:
        articles_list: A list of sources in dictionary format that contains source details. 
    Returns:
        article_results: A list of source dictionaries.
    '''
    articles_results = []

    for article in articles_list:
        id = article['source'].get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        publishedAt = article.get('publishedAt')
        image = article.get('urlToImage')
        content = article.get('content')

        # Initialize only if article has content
        if content and title:
            article_object = Article(id,author,title,description,publishedAt,image,content)
            articles_results.append(article_object)
    
    return articles_results

def get_article(id, article_title):
    '''
    Function that will request the json response of a news article.

    Args:
        id: The id of the source
        article_title: The title of the specific news article.
    
    Returns:
        article_object: Object of an article
    '''
    articles_results = get_source_articles(id)

    article_object = None

    for article in articles_results:
        if article.title == article_title:
            article_object = article
    
    return article_object






