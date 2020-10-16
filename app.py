from flask import Flask

app = Flask(__name__)

# The below line is required for csrf token.
# Ideally the secret key should be a system variable,
# but we can/are using anything here.
app.config["SECRET_KEY"] = "secret-key"

from routes import *


if __name__ == "__main__":
    app.run(debug=True)
