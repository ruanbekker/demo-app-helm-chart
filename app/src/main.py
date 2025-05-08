import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from utils.config import load_config

app = Flask(__name__)

db_url = load_config("DATABASE_URL", "sqlite:///app.db")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "defaultsecretkey")

from api.models import db, Item
db.init_app(app)

from api.routes import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

@app.route("/api/health", methods=["GET"])
def health_check():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

@app.route("/")
def home():
    items = Item.query.all()
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add_item():
    name = request.form.get("name")
    description = request.form.get("description")
    if name:
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:item_id>", methods=["POST"])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    item.name = request.form.get("name")
    item.description = request.form.get("description")
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)

