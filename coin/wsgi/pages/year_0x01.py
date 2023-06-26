# native
pass

# third-party
from flask import (
    Blueprint,
    render_template
)

# internal
pass


# establish the route register
year0x01_blueprint = Blueprint('year0x01_blueprint', __name__)

@year0x01_blueprint.route('/ucfkohzrtj', methods=['GET'])
def year0x01(): return render_template('year_0x01.html')
