from flask import render_template, redirect, url_for
from app import app, db
import forms
from models import Task
import datetime


@app.route("/")
@app.route("/index")
def index():
    tasks = Task.query.all()
    # tasks = Task.query.order_by(Task.title.desc())
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add():
    # Instantiate an object of class AddTaskForm from module forms
    form = forms.AddTaskForm()

    if form.validate_on_submit():
        print("Form submitted : ", form.title.data)
        t = Task(title=form.title.data, date=datetime.datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for("index"))
    # Pass the variable form with it's name as form (context) to the render template
    # so that we can use the variable form in the 'about.html' file.
    return render_template("add.html", form=form)
