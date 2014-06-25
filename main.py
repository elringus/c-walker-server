import webapp2
import json
from random import randint

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Panda! This is the server for the cwalker client.')

class Player(webapp2.RequestHandler):
    def get(self):
        data = json.dumps({'PlayerPosition': [randint(-24, 24), randint(-24, 24)]})
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

class Pointer(webapp2.RequestHandler):
    def get(self):
        data = json.dumps({'PointerPosition': [randint(-24, 24), randint(-24, 24)]})
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

class Obstacles(webapp2.RequestHandler):
    def get(self):
        c = {'Obstacles': []}
        for i in range(0, 100):
            c['Obstacles'].append(['house' if randint(0, 3) == 3 else 'tree', randint(-24, 24), randint(-24, 24)])
        data = json.dumps(c)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(data)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/getPointer', Pointer),
    ('/getPlayer', Player),
    ('/getObstacles', Obstacles),
], debug=True)
