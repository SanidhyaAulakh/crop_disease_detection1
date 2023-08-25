# Crop Disease Detection Web App

A web application for predicting crop disease using machine learning and deep learning techniques.
# working prototype video
https://www.loom.com/share/4dd1b0dd45e14b8d9fb8a653ebe7fe00?sid=d182a64b-998b-4597-8659-b5bee9807607
# website working project pics 
<img width="942" alt="image" src="https://github.com/SanidhyaAulakh/crop_disease_detection1/assets/143162258/ce62df16-030c-4760-8136-72536cfaebb5">

<img width="694" alt="image" src="https://github.com/SanidhyaAulakh/crop_disease_detection1/assets/143162258/c2036a52-c8af-43b7-99ea-225d38be5bc9">
<img width="768" alt="image" src="https://github.com/SanidhyaAulakh/crop_disease_detection1/assets/143162258/50b419fc-f92b-4b27-8552-893e2100d76a">


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

git clone https://github.com/SanidhyaAulakh/crop_disease_detection1.git

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
