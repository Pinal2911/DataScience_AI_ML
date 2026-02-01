from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def main_pg():
    return "<html><h1>Welcome to Flask App</h1></html>"

@app.route('/index')
def index_pg():
    return render_template('index.html')

@app.route('/about')
def about_pg():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)