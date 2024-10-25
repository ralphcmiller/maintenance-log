from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data, will integrate with dynamoDB later
vehicles = ['My 4Runner', 'Honda Civic', 'Scoot-mobile', 'HZJ73']

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify(vehicles)

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    vehicle = request.json
    vehicles.append(vehicle)
    return jsonify(vehicle), 201

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = next((v for v in vehicles if v["id"] == vehicle_id), None)
    if vehicle:
        return jsonify(vehicle)
    else:
        return jsonify({"error": "Vehicle not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')