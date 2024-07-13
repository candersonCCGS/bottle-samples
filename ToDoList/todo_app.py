from bottle import route, run, template

##################################################
#
# Constants

##################################################
#
# Routes for each page
#
# Home page
@route('/')
def index():
    return template('index')

##################################################
#
# Helper functions

##################################################
#
# Run the web server to serve up the pages
#
run(host='localhost', port=8081, debug=True, reloader=True)