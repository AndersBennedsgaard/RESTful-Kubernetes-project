from flask import Flask
from flask_restful import Api
from app.logger import log
from app.resources import Item, ShoppingList
from app.db import init_db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    log.info("Initialized app")

    api = Api(app)
    log.info("Initialized API")

    init_db(app)

    api.add_resource(ShoppingList, "/shoppinglist")
    api.add_resource(Item, "/shoppinglist/<int:item_id>")

    return app
