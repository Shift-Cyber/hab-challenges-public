# Inheretance from main
from __main__ import (
    app
)

# Python standard libraries
pass

# Third-party libraries
from flask import (
    render_template,
    request
)

# Internal imports
pass


@app.route("/nevermind", methods=["GET", "POST"])
def nevermind():
    if request.method == "GET":
        return render_template("nevermind.html")
    elif request.method == "POST":
        if request.headers.get('md5_image_hash') == "021d99868f8b0943b2cf04e944ddab8f":
            return "flag{nevermind_not_that_beautiful}\n"
        else:
            return "nope.. try again\n"
    else:
        return render_template("nevermind.html")