import webapp2
import os
import cgi
from DictionaryKinesthetic import *
    
BASEPATH = os.path.dirname(__file__)

class RestDictionaryKinesthetic(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        dict = DictionaryKinesthetic()
        output = "{"
        for element in dict.get():
            output = output + "\"" + element + "\","
        output = output + "}"
        self.response.write(output)

app = webapp2.WSGIApplication([
    ('/rest/dictionary/kinesthetic', RestDictionaryKinesthetic),
], debug=True)
