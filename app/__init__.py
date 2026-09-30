from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    from app.routes import routes
    app.register_blueprint(routes)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:TASREEE3%40s@localhost:3306/tasree3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    from app.models.models import Source , Tip
    
    with app.app_context(): 
        db.create_all()
    
    
    return app