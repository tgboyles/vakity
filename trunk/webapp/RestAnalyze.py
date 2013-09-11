import webapp2
import os
import cgi
from Analyze import *
    
BASEPATH = os.path.dirname(__file__)

class RestAnalyze(webapp2.RequestHandler):

    def post(self):
        writing_sample = self.request.get('writing_sample')
        analyzer = Analyze()
        analysis = analyzer.process(writing_sample)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(analysis)

app = webapp2.WSGIApplication([
    ('/rest/analyze', RestAnalyze),
], debug=True)
