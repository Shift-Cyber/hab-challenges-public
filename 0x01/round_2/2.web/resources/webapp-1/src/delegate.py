# Inheretance from main
from __main__ import (
    app
)

# Python standard libraries
import time
import requests

# Third-party libraries
from flask import (
    render_template,
    request
)

# Internal imports
pass


@app.route("/delegate", methods=["GET", "POST"])
def delegate():
    if request.method == "POST":
        if int(request.form.get("epoch")) == int(time.time()):
            requests.post(request.form.get('destination'), json = {'flag': 'flag{whats_good_mr_mailman}'})
            return f"yup, nice... sent the flag to: {request.form.get('destination')}"

        elif int(request.form.get("epoch")) != int(time.time()):
            return "wrong epoch dude, you're running out of *time*"

        else: return "what?"
    else:
        return render_template("delegate.html")
    