from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import joblib
from pathlib import Path
import math
import folium

app = Flask(__name__)
#función de predicción
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 6)
    HERE = Path(__file__).parent
    rfr = joblib.load(open(HERE/"modelo_entrenado.pkl", "rb"))
    result = rfr.predict(to_predict)
    return result[0]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculadora", methods=['GET'])
def form():
    if request.method == 'GET':
        return render_template("calculadora.html")

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        res_const=request.form.get("area_c")
        res_sup=request.form.get("superficie")
        res_rooms=request.form.get("rooms")
        res_brms=request.form.get("brms")
        res_prk=request.form.get("prk")
        res_ant=request.form.get("ant")
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)  
        parte_entera = math.trunc(result)             
        return render_template("result.html", prediction = parte_entera, res_sup=res_sup, res_const=res_const, res_rooms=res_rooms, res_brms=res_brms, res_prk=res_prk, res_ant=res_ant)

@app.route("/Mapa_Depas_1")
def Mapa_Depas_1():
    return render_template("Mapa_Depas_1.html")

if __name__ == "__main__":
    app.run(debug=True)