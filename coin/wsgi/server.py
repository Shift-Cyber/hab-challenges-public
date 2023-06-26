# native
import os
import sys
import logging

# third-party
import google.cloud.logging
from flask import (
    Flask,
    request,
    render_template
)

# internal
from pages.public import public_blueprint
from pages.year_0x01 import year0x01_blueprint

# setup environment and instantiate app
required_environemnt_variables = [
    'COIN_SECRET',
]

for environment_variable in required_environemnt_variables:
    if environment_variable not in os.environ:
        logging.error(f'Required environment variable {environment_variable} is missing, exiting...')
        sys.exit(-1)

DIST_LOCATION = os.environ.get("COIN_DIST_LOCATION", '../frontend/dist')

app = Flask(__name__, template_folder=DIST_LOCATION)
app.config['DIST_LOCATION'] = DIST_LOCATION
app.secret_key = os.environ.get("COIN_SECRET")

# configure logging
if bool(os.environ.get("COIN_LOG_LOCAL", 0)):
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d (%(levelname)s | %(filename)s:%(lineno)d) - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    logging.info("logging set to stdout instead of GCP")

else: google.cloud.logging.Client().setup_logging()

# extend gunicorn so that WSGI errors are logged
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)

# routes
@app.route('/', methods=['GET'])
def root(): return render_template('root.html')

# required public routes
app.register_blueprint(public_blueprint)

# yearly challenges
app.register_blueprint(year0x01_blueprint)

# catchall 404 fallback
@app.route('/<path:path>', methods=['GET'])
def catch_all(path): return render_template("404.html"), 404

# start app in debug mode if run directly without gunicorn
if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port=5000,
        debug=True
    )
