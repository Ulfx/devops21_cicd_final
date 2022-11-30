from flask import Blueprint, render_template

bp = Blueprint('cool', __name__, url_prefix='/cool')


@bp.route('/reversedadv')
def stringfuncadvanced(string="Hello World"):
    return render_template("/cool/reversed.html", string=string[::-1])


@bp.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@bp.route('/reversed')
def stringfunc(string="Hello World"):
    string = string[::-1]
    return f"<p> {string} </p>"
