from flask import Blueprint, jsonify, request
from api.models import db, Item

api_bp = Blueprint("api", __name__)

@api_bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([{ "id": item.id, "name": item.name, "description": item.description } for item in items])

@api_bp.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    new_item = Item(name=data["name"], description=data.get("description", ""))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({ "message": "Item added successfully!" }), 201

