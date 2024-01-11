from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@db:5432/test_db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity
        }

with app.app_context():
    db.create_all()

    corn = Item(name="Corn", quantity=10)
    mango = Item(name="Mango", quantity=100)

    db.session.add(corn)
    db.session.add(mango)
    db.session.commit()

@app.route('/')
def index():
    return "Welcome to Flask API!"

@app.route('/items', methods=['GET'])
def get_items():
    try:
        items = Item.query.all()
        return jsonify([item.serialize() for item in items])
    except Exception as e:
        return jsonify({'message': 'Error getting items'}), 500

@app.route('/items', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        new_item = Item(name=data['name'], quantity=data['quantity'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item added successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Error adding item'}), 500
    

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    try:
        item = Item.query.get(item_id)
        if item:
            return jsonify(item.serialize())
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Error getting item'}), 500

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    try:
        item = Item.query.get(item_id)
        if item:
            data = request.get_json()
            item.name = data.get('name', item.name)
            item.quantity = data.get('quantity', item.quantity)
            db.session.commit()
            return jsonify({'message': 'Item updated successfully'})
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Error updating item'}), 500

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'message': 'Item deleted successfully'})
        else:
            return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Error deleting item'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


