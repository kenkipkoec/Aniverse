from flask import Flask

def create_app():
    app = Flask(__name__)

    # Simple route
    @app.route('/')
    def index():
        return "Hello, Aniverse!"

    return app
