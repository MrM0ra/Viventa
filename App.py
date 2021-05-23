from flask import Flask, redirect, url_for, render_template, request, flash
from model import *
from joblib import dump, load
import sklearn as sk
import numpy as np


'''
orden: 
tipo de vivienda
habitaciones
baños
parqueaderos
area privada
area construida
estrato
pisos

, dtype=np.float64
'''

array = np.array([1.0])

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def hello_world():
	global array
	if request.method == "GET":
		return render_template('index.html')
	else:
		viv_type = request.form["viv_type"]
		if "Casa" in viv_type:
			viv_type = 1
		else:
			viv_type = 0
		rooms = (int(request.form["rooms"]))
		baths = (int(request.form["baths"]))
		lots = (int(request.form["lots"]))
		priv_area = (float(request.form["priv_area"]))
		cons_area = (float(request.form["cons_area"]))
		estrato = (int(request.form["estrato"]))
		floor = (int(request.form["floor"]))
		array = np.array([viv_type, rooms, baths, lots, priv_area, cons_area, estrato, floor])
		return redirect(url_for("prediction"))


@app.route('/prediction/')
def prediction():
	global array
	clf=load('modelo_entrenado.pkl')
	array.reshape(1, -1)
	prediccion=clf.predict(array)
	return render_template("prediction.html", args=prediccion)

if __name__ == '__main__':
	app.run(debug=True)