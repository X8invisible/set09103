from flask import Flask, redirect , url_for
app = Flask(__name__)


@app.route("/private")
def private():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    return "None shall pass"
@app.route('/')
def root():
    return "The default 'root'"
@app.route("/hello/")
def hello_world():
    return "Hello napier ;)"
@app.route("/goodbye/")
def goodbye():
    return "Execute order 66"
@app.route ('/static/img')
def static_example_img():
    start= '<img src ="'
    url= url_for ('static', filename ='vmask.jpg')
    end= '>'
    return start+url+end, 200
@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find requested page", 404
if __name__=="__main__":
    app.run(host='localhost', debug=True)
