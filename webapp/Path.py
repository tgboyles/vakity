import webapp2
import os
import cgi
    
BASEPATH = os.path.dirname(__file__)

class Path(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(BASEPATH)

        

app = webapp2.WSGIApplication([
    ('/path', Path),
], debug=True)
