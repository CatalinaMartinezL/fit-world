from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Ruta del archivo JSON
CLASSES_JSON_FILE = 'data/classes.json'

# Función para cargar clases desde el archivo JSON
def load_classes():
    if os.path.exists(CLASSES_JSON_FILE):
        with open(CLASSES_JSON_FILE, 'r') as file:
            return json.load(file)
    return []

# Función para guardar clases en el archivo JSON
def save_classes(classes):
    with open(CLASSES_JSON_FILE, 'w') as file:
        json.dump(classes, file, indent=4)

# Cargar clases al iniciar la aplicación
classes = load_classes()

# Endpoints

@app.route('/api/classes', methods=['GET'])
def get_classes():
    return jsonify(classes)

@app.route('/api/classes/<int:id>', methods=['GET'])
def get_class(id):
    class_data = next((c for c in classes if c['id'] == id), None)
    if class_data:
        return jsonify(class_data)
    return jsonify({"error": "Class not found"}), 404

@app.route('/api/classes', methods=['POST'])
def add_class():
    new_class = request.json
    if not new_class or 'name' not in new_class:
        return jsonify({"error": "Invalid data"}), 400
    new_class['id'] = len(classes) + 1  # Asignar un nuevo ID
    classes.append(new_class)
    save_classes(classes)  # Guardar la nueva clase en el archivo JSON
    return jsonify(new_class), 201

@app.route('/api/classes/<int:id>', methods=['PUT'])
def update_class(id):
    updated_class = request.json
    class_index = next((i for i, c in enumerate(classes) if c['id'] == id), None)
    if class_index is None:
        return jsonify({"error": "Class not found"}), 404
    classes[class_index].update(updated_class)
    save_classes(classes)  # Guardar los cambios en el archivo JSON
    return jsonify(classes[class_index]), 200

@app.route('/api/classes/<int:id>', methods=['DELETE'])
def delete_class(id):
    global classes
    classes = [c for c in classes if c['id'] != id]
    save_classes(classes)  # Guardar los cambios en el archivo JSON
    return jsonify({"message": "Class deleted"}), 204

@app.route('/api/gym', methods=['GET'])
def get_gyms():
    gyms = [{"id": i + 1, "name": f"Gym {chr(65 + i)}"} for i in range(7)]
    return jsonify(gyms)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    if not data or 'name' not in data or 'class_name' not in data or 'gym_name' not in data:
        return jsonify({"message": "Invalid data"}), 400
    return jsonify({"message": "Inscription successful", "data": data}), 201

@app.route('/api/classes/<string:class_name>', methods=['GET'])
def get_class_details(class_name):
    class_found = next((cls for cls in classes if cls['name'] == class_name), None)
    if class_found:
        return jsonify(class_found)
    return jsonify({"message": "Class not found"}), 404

@app.route('/api/classes/<string:class_name>', methods=['PUT'])
def update_class_by_name(class_name):
    data = request.json
    class_found = next((cls for cls in classes if cls['name'] == class_name), None)
    if not class_found:
        return jsonify({"message": "Class not found"}), 404

    # Actualiza la información de la clase
    if 'description' in data:
        class_found['description'] = data['description']
    if 'instructor' in data:
        class_found['instructor'] = data['instructor']

    save_classes(classes)  # Guarda los cambios en el archivo JSON
    return jsonify(class_found)

@app.route('/api/classes/<string:class_name>', methods=['DELETE'])
def delete_class_by_name(class_name):
    global classes
    classes = [cls for cls in classes if cls['name'] != class_name]
    save_classes(classes)  # Guarda los cambios en el archivo JSON
    return jsonify({"message": "Class deleted successfully"}), 200

@app.route('/api/signup/bulk', methods=['POST'])
def bulk_signup():
    data = request.json
    if not data or 'registrations' not in data:
        return jsonify({"message": "Invalid data"}), 400

    successful_registrations = []
    for registration in data['registrations']:
        if 'name' in registration and 'class_name' in registration and 'gym_name' in registration:
            successful_registrations.append(registration)

    return jsonify({"message": "Bulk inscription successful", "data": successful_registrations}), 201

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Fit World!"})

if __name__ == '__main__':
    app.run(debug=True)
