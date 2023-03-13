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


"""
- [easy] How a basic webserver works (html, javascript, css)
store pieces of the flag across the three files, comments or something
"""

@app.route("/detective", methods=["GET"])
def detective():
    return render_template("detective.html")