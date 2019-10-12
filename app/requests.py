from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting API key
sources_api_key = app.config['NEW_API_KEY']

# Getting the sources base url
sources_url = app.config['SOURCES_API_BASE_URL']

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
            source_results = process_results(source_results_list)
        
    return source_results

def process_results(source_list):
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



