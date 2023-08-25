from flask import Flask, request, jsonify, render_template
import requests
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load your trained model
model = load_model('model.h5')  # Update with your actual model path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'})

    img = preprocess_image(image_file)
    predictions = model.predict(img)
    top_prediction = get_top_prediction(predictions)

    return jsonify({'prediction': top_prediction})

def preprocess_image(image_file):
    img = image_file.read()
    img = image.load_img(img, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

def get_top_prediction(predictions):
    # Implement your logic to extract the top prediction here
    return 'Top Prediction Label'

if __name__ == '__main__':
    app.run(debug=True)
