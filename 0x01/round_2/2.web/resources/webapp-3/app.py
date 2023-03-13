# Native imports
import os
import sys

# Third party imports
from flask import (
    Flask,
    redirect,
    render_template
)

# Environment context
DEBUG = os.environ.get("DEBUG", False)

app = Flask(__name__, template_folder="./pages")
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(30))

# Default route
@app.route("/")
def default_route(): return redirect("/brain", code=302)

# Public resources
import src.public

# Core pages
import src.brain
import src.injector

# Catchall route
@app.route("/<path:path>", methods=["GET"])
def catch_all(path):
    return render_template("404.html"), 404


if __name__ == "__main__": app.run( debug=DEBUG, host="0.0.0.0", port=80 )
