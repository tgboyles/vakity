import webapp2
import os
import cgi
from DictionaryAuditory import *
    
BASEPATH = os.path.dirname(__file__)

class RestDictionaryAuditory(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        dict = DictionaryAuditory()
        output = "{"
        for element in dict.get():
            output = output + "\"" + element + "\","
        output = output + "}"
        self.response.write(output)

app = webapp2.WSGIApplication([
    ('/rest/dictionary/auditory', RestDictionaryAuditory),
], debug=True)
