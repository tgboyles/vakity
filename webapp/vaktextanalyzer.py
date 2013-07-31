import cgi

from google.appengine.api import users

import webapp2


MAIN_PAGE_HTML = """\
<html>
  <head>
    <title>VAK Analyzer</title>
  </head>
  <body>
    <p>Welcome to the VAK (Visual, Auditory, Kinesthetic) Text Analyzer. This is a resource to allow you to analyze a person's learning style in the VAK framework, without requiring them to undertake an evaluator test.</p>
    <p>Enter a writing sample to discover the dominant learning style of the author.</p>
    <form action="/analyze" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Analyze writing sample:"></div>
    </form>
    <p>Tip: The larger the writing sample you can provide, the more accurate results will be.</p>
  </body>
</html>
"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class Analyze(webapp2.RequestHandler):

    def post(self):

	text = cgi.escape(self.request.get('content'))
	newtext = self.process(text)

        self.response.write('<html><body>Analysis of entered text:<pre>')
        self.response.write(newtext)
        self.response.write('</pre></body></html>')


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
	




application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/analyze', Analyze),
], debug=True)
