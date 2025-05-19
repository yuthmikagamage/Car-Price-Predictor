from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('LinearRegressionModel.pk1','rb'))

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

@app.route('/predict',methods=['POST'])
def predict():
    Brand = request.form.get('Brand')
    Model = request.form.get('Model')
    YOM = int(request.form.get('YOM'))
    Fuel_Type = request.form.get('Fuel_Type')
    Mileage = int(request.form.get('kilo_driven'))
    prediction = model.predict(pd.DataFrame([[Model,Brand,YOM,Mileage,Fuel_Type]],columns=['Model','Brand','YOM','Millage(KM)','Fuel Type']))
    return str(np.round(prediction[0]))



if __name__ == "__main__":
    app.run(debug=True)