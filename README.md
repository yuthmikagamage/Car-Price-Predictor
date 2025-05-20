# Car Price Predictor

A web application that predicts car prices based on brand, model, year of manufacture, fuel type, and mileage using machine learning.

## Overview

This project is a Flask-based web application that helps users estimate the price of a car based on various features. The application uses a Linear Regression model trained on car price data to make these predictions, offering a user-friendly interface for inputting car details and receiving price estimations.

## Features

- **Dynamic Dropdown Menus**: Select a car brand and see only the relevant models for that brand
- **Responsive Design**: User-friendly interface that works on different screen sizes
- **Real-time Price Prediction**: Get instant price predictions based on your selections
- **Data-Driven Results**: Powered by machine learning model trained on real car price data

## Dataset

The model is trained on the [Car Price Prediction Dataset](https://www.kaggle.com/datasets/prasadnirmal/srilankan-second-vehiclecar-price-dataset) from Kaggle. This dataset contains information about various car brands, models, manufacturing years, fuel types, mileages, and their corresponding prices.

## Technologies Used

- **Backend**: Python, Flask, pandas, scikit-learn
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Linear Regression model

## Installation and Setup

1. Clone the repository:

   ```
   git clone https://github.com/yuthmikagamage/Vehicle_Price_Predictor.git
   cd car-price-predictor
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Run the application:

   ```
   python application.py
   ```

4. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
vehicle-price-predictor/
│
├── application.py           # Flask application file
├── LinearRegressionModel.pk1 # Trained machine learning model
├── prepared_car_price_dataset.csv # Dataset for car details
├── static/
│   └── css/
│       └── style.css       # CSS styling
├── templates/
│   └── index.html          # Main HTML template
└── README.md               # Project documentation
```

## How to Use

1. Select the brand of the car from the dropdown menu
2. Choose the model from the filtered options that appear
3. Select the manufacturing year of the car
4. Choose the fuel type
5. Enter the mileage of the car in kilometers
6. Click "Predict Price" to get the estimated price

## Model Training

The price prediction is powered by a Linear Regression model trained on car features including brand, model, year of manufacture, fuel type, and mileage. The model was trained using scikit-learn and serialized using pickle.

## Acknowledgements

- [Kaggle](https://www.kaggle.com) for providing the dataset
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [scikit-learn](https://scikit-learn.org/) for machine learning tools

```

```
