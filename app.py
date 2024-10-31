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

# Función para guardar clases en el archivo JSON (puede ser útil en el futuro)
def save_classes(classes):
    with open(CLASSES_JSON_FILE, 'w') as file:
        json.dump(classes, file, indent=4)

# Cargar clases al iniciar la aplicación
classes = load_classes()

# Endpoints

@app.route('/api/classes', methods=['GET'])
def get_classes():
    return jsonify(classes)

@app.route('/api/gym', methods=['GET'])
def get_gyms():
    # Crear una lista de gimnasios ficticios
    gyms = [{"id": i + 1, "name": f"Gym {chr(65 + i)}"} for i in range(7)]
    return jsonify(gyms)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    # Validar la entrada de datos
    if not data or 'name' not in data or 'class_name' not in data or 'gym_name' not in data:
        return jsonify({"message": "Invalid data"}), 400

    # Aquí puedes manejar la lógica para guardar la inscripción
    # Por ahora, solo vamos a devolver los datos recibidos
    return jsonify({"message": "Inscription successful", "data": data}), 201

# Ruta para la página de inicio (opcional)
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Fit World!"})

if __name__ == '__main__':
    app.run(debug=True)
