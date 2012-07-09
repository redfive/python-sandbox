#!/usr/bin/env python

import web

urls = ( '/', 'index',
         '/\(redfive\).*/' 'hello' )

class index:
    def GET(self):
        return "Hello, world!"

class hello:
    def GET(self, name):
        return "Hello" + name

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    print "end main"
