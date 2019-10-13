class News_Article:
    '''
    Class to create the news article instances. 
    '''
    def __init__(self,id,author,title,description,publishedAt,image,content,url):
        '''
        '''
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.image = image
        self.content = content
        self.url = url
