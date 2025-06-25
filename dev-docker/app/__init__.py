from flask import Flask # type: ignore

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../.env', silent=True)

    from .routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app