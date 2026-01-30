from flask import Flask

#app is an instance of flask class
'''
it creates an instance of flask class, which will be your WSGI application
'''
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to home and welcome page"

@app.route("/index")
def index_page():
    return "welcome to index page"


if __name__=="__main__":
    '''
    with help of run we started the app and degub true auto refreshes the server upon changes
    '''
    app.run(debug=True)


