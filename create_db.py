"""
 CAUTION
 Run this script only once.
 Else it will overwrite your current database.
"""

from app import db
from models import Task
import datetime

# Create database
db.create_all()

# Above line has already created your database.
# The lines below just checks if every is working alright
# by adding dummy data and printing it.

# Create an instance/object of db model
t = Task(title="xyz", date=datetime.datetime.utcnow())
print("t.__repr__(): ", t)
#t.__repr__()

# Add that instance/object to db
db.session.add(t)

# Commit to the database
db.session.commit()

# Create another instance, add to the database & commit to database
t = Task(title="abc", date=datetime.datetime.utcnow())
db.session.add(t)
db.session.commit()

# Get all rows from database and print
task_list = Task.query.all()
print("task_list: ", task_list)