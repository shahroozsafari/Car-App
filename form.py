import flask_wtf
import wtforms

class CarEntryForm(flask_wtf.Form):
    carid=wtforms.IntegerField("Car ID")
    brand=wtforms.StringField("Brand")
    model=wtforms.StringField("Model")
    year=wtforms.IntegerField("Year")
    price=wtforms.IntegerField("Price")
    submit=wtforms.SubmitField("Save car")


form=CarEntryForm()
