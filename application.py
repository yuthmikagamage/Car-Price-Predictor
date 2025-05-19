from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)
car = pd.read_csv("prepared_car_price_dataset.csv")

@app.route('/')
def index():
    Brand = car['Brand'].unique()
    Model = sorted(car['Model'].unique())
    YOM = sorted(car['YOM'].unique(), reverse=True)
    Fuel_Type = sorted(car['Fuel Type'].unique())
    return render_template('index.html', Brand=Brand, Model=Model, YOM=YOM, Fuel_Type=Fuel_Type)

@app.route('/get_models/<brand>')
def get_models(brand):
    brand_models = sorted(car[car['Brand'] == brand]['Model'].unique())
    return jsonify(models=brand_models)

if __name__ == "__main__":
    app.run(debug=True)