from flask import Blueprint # type: ignore

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Hello from Flask!'