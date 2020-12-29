import os
from flask_sqlalchemy import SQLAlchemy
from app.logger import log

db = SQLAlchemy()


def init_db(app, testing):
    db.init_app(app)
    if testing or not os.path.isfile("app/database.db"):
        with app.app_context():
            db.create_all()
        log.warning("Created database from scratch")
    else:
        log.info("Initialized database")


class ItemModel(db.Model):
    """
    SQL Alchemy database model of an item in a shopping list.
    Have columns containing: id, name, quantity and some note
    """

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # db.String(100): maximum 100 character string.
    # nullable=False: name must be defined
    quantity = db.Column(db.String(20), nullable=True)
    note = db.Column(db.String(100), nullable=True)

    def __repr__(self) -> str:
        return f"Item(id={self.item_id}, name={self.name}, quantity={self.quantity}, note={self.note})"
