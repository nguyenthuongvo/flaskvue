from flask import Flask, jsonify, request
from flask_cors import CORS
import os

if __name__ == '__main__':

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    # register the database commands
    from core import db

    db.init_app(app)

    from core import auth, blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    app.run()