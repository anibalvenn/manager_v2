from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configure the static URL path and folder
    app.static_url_path = '/static'
    app.static_folder = 'static'

    from app.routes import init_routes
    init_routes(app)

    return app
