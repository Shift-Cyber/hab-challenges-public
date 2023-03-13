# Inheretance from main
from __main__ import (
    app
)

# Python standard libraries
pass

# Third-party libraries
import mysql.connector
from flask import (
    render_template,
    request
)

# Internal imports
pass


@app.route("/injector", methods=["GET", "POST"])
def injector():
    username = request.form.get("user")
    password = request.form.get("pass")

    connector = mysql.connector.connect(
        host = "localhost",
        user = "webapp2user",
        password = "password123",
        database = "webapp2"
    )

     # make db call
    cursor = connector.cursor(prepared=True)


    # heres the injection
    user_tuple = None
    try:
        # this is obviously rediculous, not even hashing the payload for comparison
        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND pwhash='{password}'")

        # gonna get them all, cause sure why not, in this made up farytale world
        user_tuple = cursor.fetchall()

        cursor.close()

        if user_tuple:
            # this is still not real at all but it gets the job done
            response_data = f"Welcome {user_tuple}!"
        else:
            response_data = f"Login failed!"
        
    except:
        response_data = f"Thats weird... something broke..."

    return render_template("injector.html", response_data=response_data)
