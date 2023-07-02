from flask import Flask, jsonify, request
from api.controllers import detect_disease_from_image

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to Eye Disease Detection API!'
    })

@app.route('/detection', methods=['POST'])
def detect_disease():
    image = request.files['image']
    disease = detect_disease_from_image(image)
    return jsonify({
        'disease': disease
    }), 200
