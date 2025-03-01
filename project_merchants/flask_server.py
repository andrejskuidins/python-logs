import json
from flask import Flask, jsonify, request

CONFIG_MERCH = 'merchant_list.config'
CONFIG_TRANS = 'merchant_trans.config'

app = Flask(__name__)

@app.route('/health_check')
def hello_world():
    return jsonify(message="ok")

with open(CONFIG_MERCH, 'r') as f:
    merchants = json.load(f)

# In-memory data store
with open(CONFIG_TRANS, 'r') as f:
    items = json.load(f)

# GET request: Retrieve all items
@app.route('/merchants', methods=['GET'])
def get_merchants():
    return jsonify(merchants)

# GET request: Retrieve a specific item by ID
@app.route('/merchants/<string:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# POST request: Create a new item
@app.route('/merchants', methods=['POST'])
def create_item():
    new_item = {"id": len(items) + 1, "name": request.json.get('name')}
    items.append(new_item)
    return jsonify(new_item), 201

# PUT request: Update an existing item
@app.route('/merchants/<string:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    item['name'] = request.json.get('name', item['name'])
    return jsonify(item)

# DELETE request: Delete an item
@app.route('/merchants/<string:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)