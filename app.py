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
        try:
            Car(car['carid'],car['brand'],car['model'],car['year'],car['price'])
        except:
            return flask.render_template('error.html')
        return flask.render_template('/index.html')
    return flask.render_template("/newcar.html")

@app.route('/carslist')
def carslist():
    return flask.render_template('carslist.html',allcars=list(Car.list()))

app.run(debug=True)
