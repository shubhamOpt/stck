########## News API ########################################################
import json
import sys
from imp import reload
from newsapi import NewsAPI

key = '7b16a116fb524a6d953145b2e3ff20cc'
params = {}
api = NewsAPI(key)
sources = api.sources(params)
articles = api.articles(sources[0]['id'], params)

################ NY Times API #############################################




reload(sys)

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
#sys.setdefaultencoding('utf8')
#sys.set
import requests
"""
About:
Python wrapper for the New York Times Archive API 
https://developer.nytimes.com/article_search_v2.json
"""


class APIKeyException(Exception):
    def __init__(self, message): self.message = message


class InvalidQueryException(Exception):
    def __init__(self, message): self.message = message


class ArchiveAPI(object):
    def __init__(self, key=None):
        """
        Initializes the ArchiveAPI class. Raises an exception if no API key is given.
        :param key: New York Times API Key
        """
        self.key = key
        self.root = 'http://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}'

        #request_string
        if not self.key:
            nyt_dev_page = 'http://developer.nytimes.com/docs/reference/keys'
            exception_str = 'Warning: API Key required. Please visit {}'
            raise NoAPIKeyException(exception_str.format(nyt_dev_page))

    def query(self, year=None, month=None, key=None, ):
        """
        Calls the archive API and returns the results as a dictionary.
        :param key: Defaults to the API key used to initialize the ArchiveAPI class.
        """
        if not key: key = self.key
        if (year < 1882) or not (0 < month < 13):
            # currently the Archive API only supports year >= 1882
            exception_str = 'Invalid query: See http://developer.nytimes.com/archive_api.json'
            raise InvalidQueryException(exception_str)
        url = self.root.format(year, month, key)
        r = requests.get(url)
        return r.json()


api = ArchiveAPI('7b16a116fb524a6d953145b2e3ff20cc')

#years = [2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007]
years = [2011]
#months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months = [11]



for year in years:
    for month in months:
        mydict = api.query(year, month)
        #file_str = '/Users/Shubham/Documents/Project Stock predictions/data/nytimes/' + str(year) + '-' + '{:02}'.format(
         #   month) + '.json'
        file_str = open("/Users/Shubham/Documents/Project Stock predictions/data/nytimes " + str(year) + "-" + "{:02}".format(
            month) + ".json", "w")
        with file_str as fout:
            json.dump(mydict, fout)
        fout.close()