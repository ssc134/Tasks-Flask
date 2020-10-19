# FlaskForm class is the base class for all forms
from flask_wtf import FlaskForm


# StringField is same as textfield in html
# SubmitField is same as submit button field in html
from wtforms import StringField, SubmitField


# The DataRequired class is used when we don't want input to be empty.
from wtforms.validators import DataRequired

# create a class to create forms
# AddTaskForm class extends/inherits from FlaskForm class
class AddTaskForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class DeleteTaskForm(FlaskForm):
    submit = SubmitField(label="Delete")