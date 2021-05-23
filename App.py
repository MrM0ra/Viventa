from flask import Flask, redirect, url_for, render_template, request, flash
from model import *
from joblib import dump, load
import sklearn as sk
import numpy


'''
#orden: 
tipo de vivienda
habitaciones
baños
parqueaderos
area privada
area construida
estrato
pisos
'''

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def hello_world():
	if request.method == "GET":
		return render_template('index.html')
	else:
		#currentuser = request.args.get("currentuser")
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
		arr = [viv_type, rooms, baths, lots, priv_area, cons_area, estrato, floor]
		return redirect(url_for("prediction", args=arr, code=307))

@app.route('/prediction/<args>')
def prediction(args):
	clf=load('modelo_entrenado.pkl')
	a = numpy.asarray(args, dtype="float64", order=None, like=None)
	prediccion=clf.predict(a)
	return render_template("prediction.html", args=prediccion)

if __name__ == '__main__':
	app.run(debug=True)