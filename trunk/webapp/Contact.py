from google.appengine.api import mail
import os
import urllib
import jinja2
import webapp2

    
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class Contact(webapp2.RequestHandler):
     
    def get(self):
        template_values = {
            'foo': 'bar'
        }
         
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.write(template.render(template_values))   
      
    def post(self):
        first_name = self.request.get('first_name')
        last_name = self.request.get('last_name')
        email = self.request.get('email')
        comments = self.request.get('comments')
                 
        send_mail(first_name, last_name, email, comments)
        
        template_values = {
            'foo': 'bar'
        }
          
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.write(template.render(template_values))

    def send_mail(self, first_name, last_name, email, comments):
        mail.send_mail(sender=email,
            to="Margeaux Bucher <mxbucher@gmail.com>",
            subject="Contact from Vakity Web App: " + first_name + " " + last_name,
            body=comments)
  

app = webapp2.WSGIApplication([
    ('/contact', Contact),
], debug=True)
