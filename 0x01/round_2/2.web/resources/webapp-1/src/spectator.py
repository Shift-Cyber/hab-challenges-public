# Inheretance from main
from __main__ import (
    app
)

# Python standard libraries
pass

# Third-party libraries
from flask import (
    render_template,
    make_response
)

# Internal imports
pass


"""
- [easy] Browser tools (inspect element, networking, cookies)
store a flag in a cookie or other header and force them to find something not in a page resource
spread across a couple things here
"""

@app.route("/spectator", methods=["GET"])
def spectator():
    resp = make_response(render_template("spectator.html"))
    resp.set_cookie('flag_stuff', '_many_ways_to')
    resp.headers['more_flag_stuff'] = '_manage_data}'

    return resp