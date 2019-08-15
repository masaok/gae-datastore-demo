import webapp2
import os
import jinja2
from models import Student, Wand, House, Course, Enrollment, Teacher
from seed import seed_data

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write('Thank you. The Datastore is now seeded.')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/seed', LoadDataHandler)
], debug=True)
