# Inheretance from main
from __main__ import (
    app
)

# Python standard libraries
pass

# Third-party libraries
from flask import (
    render_template
)

# Internal imports
pass


@app.route("/vision", methods=["GET"])
def vision():
    return render_template("vision.html")
