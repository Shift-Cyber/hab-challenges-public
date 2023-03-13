# Inheretance from main
from __main__ import (
    app
)

# Python standard libraries
pass

# Third-party libraries
from flask import (
    render_template,
    request,
    make_response,
    Response
)

# Internal imports
import jwt


@app.route("/brain", methods=["GET"])
def brain():
    level = 0
    secret_number = "What?"
    checks = {'header':False, 'url-1':False, 'url-2':False, 'jwt':False}

    # 1. check header
    if request.headers.get('flag-sauce') == 'habanero':
        level += 1
        checks['header'] = True

    # 2. check secret int
    try:
        secret_number = int(request.args.get('my-int'))
    except:
        secret_number = "no"

    if secret_number == 72:
        level += 1
        checks['url-1'] = True

    # 3. check secret int
    if request.args.get('give-me-that-flag') == "hand-it-over":
        level += 1
        checks['url-2'] = True
    
    # 4. check jwt
    try:
        auth_header = request.cookies.get('Authentication').split(' ')[1]
        auth_header_decoded = jwt.decode(auth_header, options={"verify_signature": False})

        if auth_header_decoded['admin'] == 'true':
            level += 1
            checks['jwt'] = True
    except: pass


    response = make_response(
        render_template(
            "brain.html",
            level=level,
            secret_number=secret_number,
            checks=checks
        )
    )

    if not checks['header']:
        response.headers.set('fLaG-sAuCe', 'lol no')
    
    if not checks['jwt']:
        response.set_cookie('Authentication', 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOiJmYWxzZSJ9.lq4IQYyT1PxeSQ89DB7pu9i3rPEdPDAQtiSKJSk9VVo')

    return response

