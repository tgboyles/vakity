import webapp2
import os
import urllib
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class Analyze(webapp2.RequestHandler):

    def get(self):
        template_values = {'analysis': "nothing"}     
        template = JINJA_ENVIRONMENT.get_template('VAK_tool.html')
        self.response.write(template.render(template_values))
        
    def post(self):
        writing_sample = self.request.get('writing_sample')
      
        # Here we process the text
        analysis = self.process(writing_sample)
         
        template_values = {'analysis': analysis}     
        template = JINJA_ENVIRONMENT.get_template('VAK_tool.html')
        self.response.write(template.render(template_values))


    def process(self, text):
	
	
	visual_dictionary = ("see", 
                         "look", 
                         "appear", 
                         "foggy", 
                         "see eye to eye", 
                         "in light of", 
                         "get a mental picture", 
                         "you can plainly see", 
                         "clear cut", "appears", 
                         "make a scene", 
                         "my perspective", 
                         "under your nose", 
                         "test_test")

	auditory_dictionary = ("hear", 
                           "listen", 
                           "sounds", 
                           "deaf", 
                           "describe", 
                           "as a manner of speaking", 
                           "just idle talk", 
                           "that rings a bell", 
                           "clear as a bell", 
                           "earful", 
                           "tounge-tied", 
                           "tounge tied", 
                           "pay more attention to", 
                           "hold your tounge", 
                           "heard voices", 
                           "hearing voices", 
                           "within hearing range" )
    
   	
	kinesthetic_dictionary = ("feel", 
                              "touch", 
                              "get ahold of", 
                              "hard", 
                              "get a load of this", 
                              "sharp as a tack", 
                              "feeling", 
                              "hot headed", 
                              "hot-headed", 
                              "pain in the neck", 
                              "pain in the butt", 
                              "pain in the ass", 
                              "pain in the arse", 
                              "boils down to", 
                              "get a grip on", 
                              "starting from scratch", 
                              "keep your shirt on", 
                              "panties in a twist", 
                              "get in touch with", 
                              "make a leap",
                              "slipped my mind" )
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
	per_visual = int((float(visual_counter) / float(total) * 100) + .5)
	per_auditory = int((float(auditory_counter) / float(total) * 100) + .5)
	per_kinesthetic = int((float(kinesthetic_counter) / float(total) * 100) + .5)



    

	analysis = str(total) + " Keywords and/or indicator phrases found." + "<br><br><br>" + str(visual_counter) + " Visual indicators.<br>" + str(auditory_counter) + " Auditory indicators.<br>" + str(kinesthetic_counter) + " Kinesthetic indicators.<br><br><br>" + str(per_visual) + "%" + " Visual<br>" + str(per_auditory) + "%" + " Auditory<br>" + str(per_kinesthetic) + "%" + " Kinesthetic"
	return analysis
	


app = webapp2.WSGIApplication([
    ('/Analyze', Analyze),
], debug=True)
