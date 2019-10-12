import unittest
from models import source 

Source = source.Source

class Source_Test(unittest.TestCase):
    '''
    Source test class to test the behavior of Source class.
    '''
    def setUp(self):
        '''
        Set up method to create an instance of a source before any test.
        '''
        self.new_source = Source("abc-news","ABC NEWS","Your trusted source for breaking news and analysis.")
    
    def test_instance(self):
        '''
        Test instance method to test if objects are iniatialized properly.
        '''
        self.assertTrue(isinstance(self.new_source, Source))

if __name__== '__main__':
    unittest.main()
