from flask import Flask, redirect, url_for, render_template, request, flash
import sklearn

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def hello_world():
	if request.method == "GET":
		return render_template('index.html')
	else:
		#currentuser = request.args.get("currentuser")
		viv_type = request.form["viv_type"]
		rooms = request.form["rooms"]
		baths = request.form["baths"]
		lots = request.form["lots"]
		priv_area = request.form["priv_area"]
		cons_area = request.form["cons_area"]
		estrato = request.form["estrato"]
		floor = request.form["floor"]
		arr = [viv_type, rooms, baths, lots, priv_area, cons_area, estrato, floor]
		print(arr)
		return redirect(url_for("prediction", args=arr, code=307))

@app.route('/prediction/<args>')
def prediction(args):
	print(args)
	return render_template("prediction.html", args=args)

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


if __name__ == '__main__':
	app.run(debug=True)