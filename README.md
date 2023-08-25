# Crop Disease Detection Web App

A web application for predicting crop disease using machine learning and deep learning techniques.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a web application built using Flask, TensorFlow, and the Hugging Face Model Hub API. It allows users to upload images of plants and predicts whether the plants are healthy or diseased.

## Project Structure

project_directory/
│ app.py
│
└───static/                             
│ │ styles.css
│ │ script.js
│
└───templates/
│ │ index.html
│
└───model.h5

- `app.py`: The main Flask application file containing the web routes and prediction logic.
- `static/`: Folder containing static files like CSS and JavaScript.
- `templates/`: Folder containing HTML templates.
- `model.h5`: Trained machine learning model.

## Installation

1. Clone the repository:

git clone https://github.com/your-username/crop-disease-detection.git

2. Install the required libraries using pip:

pip install flask requests tensorflow

## Usage

1. Run the Flask development server:

flask run

2. Access the web app by opening a browser and navigating to `http://127.0.0.1:5000`.

3. Upload an image of a plant and click the "Predict" button to see the disease prediction.

## Contributing

Contributions are welcome! If you find a bug or have a feature suggestion, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
