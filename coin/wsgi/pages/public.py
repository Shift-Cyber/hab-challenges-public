# native
pass

# third-party
from flask import (
    Blueprint,
    send_from_directory,
    current_app
)

# internal
pass


# establish the route register
public_blueprint = Blueprint('public', __name__)


@public_blueprint.route('/css/<path:filename>')
def assets_css(filename:str): return send_from_directory(f"{current_app.config['DIST_LOCATION']}/css/", filename)

@public_blueprint.route('/js/<path:filename>')
def assets_js(filename:str): return send_from_directory(f"{current_app.config['DIST_LOCATION']}/js/", filename)

@public_blueprint.route('/fonts/<path:filename>')
def assets_fonts(filename:str): return send_from_directory(f"{current_app.config['DIST_LOCATION']}/fonts/", filename)

@public_blueprint.route('/img/<path:filename>')
def assets_img(filename:str): return send_from_directory(f"{current_app.config['DIST_LOCATION']}/img/", filename)

@public_blueprint.route('/favicon.png')
def assets_logo(): return send_from_directory(f"{current_app.config['DIST_LOCATION']}/", 'favicon.png')
