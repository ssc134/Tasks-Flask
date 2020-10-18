from app import db

# Similar to using wtforms module, we are using
# SQLAlchemy and writing our functionality on top of that

# create a database model named Task
# It inherits/extends db.Model class
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=True)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return(f"{self.title} created on date {self.date}")