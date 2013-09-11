import webapp2
import os
import cgi
from DictionaryVisual import *
    
BASEPATH = os.path.dirname(__file__)

class RestDictionaryVisual(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        dict = DictionaryVisual()
        output = "{"
        for element in dict.get():
            output = output + "\"" + element + "\","
        output = output + "}"
        self.response.write(output)

app = webapp2.WSGIApplication([
    ('/rest/dictionary/visual', RestDictionaryVisual),
], debug=True)
