from flask import Blueprint, g, render_template

bp = Blueprint('cool', __name__, url_prefix='/cool')


@bp.route('/reversed')
def coolfunc(string="Hello World"):
    return render_template("/cool/reversed.html", string=string[::-1])
