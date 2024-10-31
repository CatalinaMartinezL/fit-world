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

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Fit World!"})

if __name__ == '__main__':
    app.run(debug=True)
