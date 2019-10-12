class Source:
    '''
    Class to create the news source instances. 
    '''
    def __init__(self, id, name, description):
        '''
        Initilization method to instantiate Source objects.

        Args:
            id: The unique identification of Source object.
            name: The name of the Source object
            description: The description of the Source object
        '''
        self.id = id
        self.name = name
        self.description = description