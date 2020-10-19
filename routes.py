from flask import render_template, redirect, url_for, flash, get_flashed_messages
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
        flash("Task added to database")
        return redirect(url_for("index"))
    # Pass the variable form with it's name as form (context) to the render template
    # so that we can use the variable form in the 'about.html' file.
    return render_template("add.html", form=form)


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.datetime.utcnow()
            db.session.commit()
            flash("Task has been updated")
            return redirect(url_for("index"))
        form.title.data = task.title
        return render_template("edit.html", form=form, task_id=task_id)
    else:
        flash("Task not found.")
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["GET", "POST"])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Task has been deleted")
            return redirect(url_for("index"))
        return render_template("delete.html", form=form, title=task.title, task_id=task_id)
    else:
        flash("Task not found.")
    return redirect(url_for("index"))