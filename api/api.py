import os
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from logger import log


# App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
log.info("Created app")

api = Api(app)
log.info("Created API")

db = SQLAlchemy(app)


class ItemModel(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(100), nullable=False
    )  # db.String(100) = maximum 100 character string. nullable=False, name must be defined
    quantity = db.Column(db.String(20), nullable=True)
    note = db.Column(db.String(100), nullable=True)

    def __repr__(self) -> str:
        return f"Item(id={self.item_id}, name={self.name}, quantity={self.quantity}, note={self.note})"


if not os.path.isfile("database.db"):
    db.create_all()
    log.warning("Created database")


# def abort_if_item_doesnt_exist(item_id):
#     result = ItemModel.query.filter_by(id=item_id).first()
#     if not result:
#         abort(404, message=f"Item with it {item_id} does not exist!")


# def abort_if_item_exist(item_id):
#     result = ItemModel.query.filter_by(id=item_id).first()
#     if result:
#         abort(409, message=f"Item with it {item_id} already exist!")


parser = reqparse.RequestParser()
parser.add_argument(
    "name", required=True, type=str, help="Name of the item is required"
)
parser.add_argument("quantity", required=False, type=str)
parser.add_argument("note", required=False, type=str)
arg_names = [arg.name for arg in parser.args]

item_fields = {
    "name": fields.String,
    "quantity": fields.String,
    "note": fields.String,
}

# Show/delete/update(put) a single shopping list item
class Item(Resource):
    @marshal_with(item_fields)
    def get(self, item_id):
        if item_id == -1:
            log.debug("GET last inputted item")
            item_id = db.session.query(db.func.max(ItemModel.item_id)).scalar()
        else:
            log.debug(f"GET item {item_id}")
        # Creates instance of the class. Not serializable. Marshal_with creates a serializable resource
        item = ItemModel.query.filter_by(item_id=item_id).first()
        if item is None:
            abort(404, message=f"Item with ID {item_id} not found")
        return item

    @marshal_with(item_fields)
    def put(self, item_id):
        # update

        args = parser.parse_args()
        item = ItemModel.query.filter_by(item_id=item_id).first()
        if args["name"] is not None:
            item.name = args["name"]
        if args["quantity"] is not None:
            item.quantity = args["quantity"]
        if args["note"] is not None:
            item.note = args["note"]
        db.session.commit()

        return item, 201

    def delete(self, item_id):
        item = ItemModel.query.filter_by(item_id=item_id).first()
        db.session.delete(item)
        db.session.commit()
        return "", 204


# Show the entire shopping list, and add new items
class ShoppingList(Resource):
    @marshal_with(item_fields)
    def get(self):
        result = ItemModel.query.all()
        return result

    @marshal_with(item_fields)
    def post(self):
        args = parser.parse_args()
        item = ItemModel(
            name=args["name"], quantity=args["quantity"], note=args["note"]
        )
        db.session.add(item)
        db.session.commit()
        log.info(f"Added item with id {item.item_id} with name {item.name}")

        return item, 201


api.add_resource(ShoppingList, "/shoppinglist")
api.add_resource(Item, "/shoppinglist/<int:item_id>")

if __name__ == "__main__":
    app.run(debug=True)
