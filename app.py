import flask
from model import Car

app=flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/about')
def about():
    return flask.render_template("about.html")
    
@app.route('/newcar' , methods=["POST" , "GET"])
def newcar():
    if flask.request.method == "POST":
        car=dict(flask.request.form)
        Car(car['carid'],car['brand'],car['model'],car['year'],car['price'])
        return flask.render_template('/index.html')
    return flask.render_template("/newcar.html")

app.run(debug=True)
