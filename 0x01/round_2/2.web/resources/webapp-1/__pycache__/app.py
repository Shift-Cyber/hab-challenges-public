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
FLAG_BRK00_SPECTATOR = os.environ.get("FLAG_BRK00_SPECTATOR")
FLAG_5AHCX_NEVERMIND = os.environ.get("FLAG_5AHCX_NEVERMIND")
FLAG_9FHJZ_DELEGATE  = os.environ.get("FLAG_9FHJZ_DELEGATE")
DEBUG = os.environ.get("DEBUG", False)

app = Flask(__name__, template_folder="./pages")
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(30))

# Default route
@app.route("/")
def default_route(): return redirect("/detective", code=302)

# Public resources
import src.public

# Core pages
import src.detective
import src.delegate
import src.nevermind
import src.spectator

# Catchall route
@app.route("/<path:path>", methods=["GET"])
def catch_all(path):
    return render_template("404.html"), 404


if __name__ == "__main__": app.run( debug=DEBUG, host="0.0.0.0", port=80 )

"""
- [medium] Request types
have the user to GET an image or other file and then PUT it back

- [medium] Requestbin or portforwarding to receive a proxy
ideally the user would be the requestbins link in the site and then receive the flag at their target
"""