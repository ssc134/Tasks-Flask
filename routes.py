from flask import render_template
from app import app
import forms


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about", methods=["GET", "POST"])
def about():

    # Instantiate an object of class AddTaskForm from module forms
    form = forms.AddTaskForm()

    if form.validate_on_submit():
        print("Form submitted : ", form.title.data)
        return render_template("about.html", form=form, title=form.title.data)
    # Pass the variable form with it's name as form (context) to the render template
    # so that we can use the variable form in the 'about.html' file.
    return render_template("about.html", form=form)