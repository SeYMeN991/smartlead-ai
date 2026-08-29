from flask import Flask
from flask_cors import CORS
from app.database import init_db
from app.routes import web_bp,api_bp

def create_app():
    app = Flask(__name__)

    app.json.ensure_ascii = False
    app.config.from_object("config")

    CORS(app, origins=[
        "https://hamizogluseymen.wixsite.com"
    ])

    with app.app_context():
        init_db(app)

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)

    @app.route("/health")
    def health():
        return {"status":"ok"}

    return app