from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create flask app
app = Flask(__name__)

# The below line is required for csrf token.
# Ideally the secret key should be a system variable,
# but we can/are using anything here.
app.config["SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# Disable midification tracking as it causes significant overheads
# and it will be disabled by default from future releases
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

# Create an instance of the database.
db = SQLAlchemy(app)


from routes import *


if __name__ == "__main__":
    app.run(debug=True)
