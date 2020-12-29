from flask import Flask, jsonify
from flask_restful import Api
from app.logger import log
from app.resources import Item, ShoppingList
from app.db import init_db


def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
        app.config["TESTING"] = True
        log.warning("App is in testing mode")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    log.info("Initialized app")

    api = Api(app)
    log.info("Initialized API")

    init_db(app, testing)

    api.add_resource(ShoppingList, "/shoppinglist")
    api.add_resource(Item, "/shoppinglist/<int:item_id>")

    @app.route("/health")
    def health_check():
        return jsonify("healthy")

    return app
