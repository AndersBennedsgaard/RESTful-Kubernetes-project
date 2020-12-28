from flask_restful import Resource, reqparse, fields, marshal_with, abort
from app.logger import log
from app.db import db, ItemModel


parser = reqparse.RequestParser()
parser.add_argument(
    "name", required=True, type=str, help="Name of the item is required"
)
parser.add_argument("quantity", required=False, type=str)
parser.add_argument("note", required=False, type=str)

item_fields = {
    "name": fields.String,
    "quantity": fields.String,
    "note": fields.String,
}


# Show/delete/update(put) a single shopping list item
class Item(Resource):
    """
    Item RESTful API. Accesses singular items in the shopping list database
    """

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
