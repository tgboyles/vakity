import os
import urllib
import jinja2
import webapp2
from DictionaryVisual import *
from DictionaryAuditory import *
from DictionaryKinesthetic import *
    
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class Analyze(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'analysis': "&nbsp;"
        }
        
        template = JINJA_ENVIRONMENT.get_template('/analyze.html')
        self.response.write(template.render(template_values))
                
    def post(self):
        writing_sample = self.request.get('writing_sample')
      
        # Here we process the text
        analysis = self.process(writing_sample)
         
        template_values = {
            'analysis': analysis
        }
         
        template = JINJA_ENVIRONMENT.get_template('/analyze.html')
        self.response.write(template.render(template_values))


    def process(self, text):
	
        visual_dictionary = DictionaryVisual().get()     
        auditory_dictionary = DictionaryAuditory().get()
    	kinesthetic_dictionary = DictionaryKinesthetic().get()

    	visual_counter = 0
    	for word in visual_dictionary:
            	visual_counter = visual_counter + text.count(word) 
    	
    	auditory_counter = 0
    	for word in auditory_dictionary:
            	auditory_counter += text.count(word)
    
     	kinesthetic_counter = 0
    	for word in kinesthetic_dictionary:
            	kinesthetic_counter += text.count(word)
    	
    	total = visual_counter + auditory_counter + kinesthetic_counter
    	
    	#Calculate Percentages:
        per_visual = 0
        if visual_counter > 0:
            per_visual = int((float(visual_counter) / float(total) * 100) + .5)
        per_auditory = 0
        if auditory_counter > 0:    
    	       per_auditory = int((float(auditory_counter) / float(total) * 100) + .5)
        per_kinesthetic = 0
        if kinesthetic_counter > 0:
    	       per_kinesthetic = int((float(kinesthetic_counter) / float(total) * 100) + .5)
    
    
        analysis = str(total) + " Keywords and/or indicator phrases found.<br/><br/><br/>" + str(visual_counter) + " Visual indicators.<br/>" + str(auditory_counter) + " Auditory indicators.<br>" + str(kinesthetic_counter) + " Kinesthetic indicators.<br/><br/><br/>" + str(per_visual) + "%" + " Visual<br/>" + str(per_auditory) + "%" + " Auditory<br/>" + str(per_kinesthetic) + "%" + " Kinesthetic"
        return analysis



app = webapp2.WSGIApplication([
    ('/analyze', Analyze),
], debug=True)
