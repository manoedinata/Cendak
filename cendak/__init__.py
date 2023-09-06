from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "LmaoPisanKang"

    # Main
    from .routes import routes_main
    app.register_blueprint(routes_main, url_prefix="/")

    # Redirect
    from .routes import routes_redirect
    app.register_blueprint(routes_redirect, url_prefix="/r/")

    return app
