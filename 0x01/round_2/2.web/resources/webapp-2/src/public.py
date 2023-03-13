# Inheretance from main
from __main__ import (
    app
)

# Python standard libraries
pass

# Third-party libraries
from flask import (
    send_from_directory
)

# Internal imports
pass


@app.route("/css/<path:filename>")
def public_css(filename:str):
    print(filename)
    return send_from_directory("./css/", filename)

@app.route("/img/<path:filename>")
def public_img(filename:str):
    return send_from_directory("./img/", filename)

@app.route("/js/<path:filename>")
def public_js(filename:str):
    return send_from_directory("./js/", filename)
