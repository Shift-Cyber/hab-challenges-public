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


@app.route("/detour", methods=["GET"])
def detour():
    return render_template("detour.html")
