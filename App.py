"""
Initial imports to be used alongside the project
----------------------------------
	* **Flask:** Framework used to handle requests
	* **Joblib:** Library used to load a previously saved model
	* **numpy:** Library used to pass the information given by the user to the model previously loaded by Joblib
"""
from flask import Flask, redirect, url_for, render_template, request, flash
from joblib import dump, load
import numpy as np

"""
**array:** Initial NumPy Array that will be filled with 
the users information from the frontend
"""
array = np.array([[1.0]])

"""
**app:** Instance for the flask framework to be runned
"""
app = Flask(__name__)

"""
**landing_page():** Stablishes the landing page for the web deployment of the app
* **Methods:** The methods are set as POST and GET.
	* *GET:* On a get request we will load the landing page with empty fields for the user to fill them
	* *POST:* On a post request we will save the information given on the frontend by the user and will pass it to the AI model to use them as input parameters ang give us a response (prediction)
"""
@app.route('/', methods=["POST", "GET"])
def landing_page():
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
		array = np.array([[viv_type, rooms, baths, lots, priv_area, cons_area, estrato]])
		return redirect(url_for("prediction"))

"""
**prediction():** Sets up the result page for the web deployment of the app
**Usage:** This method loads the previously save AI model, then gets the global array that already hast the values setted by the user on the landing page and reshapes it to be able to use it on the model. Then asks the model for a prediction on the given user data and shows it on screen
"""
@app.route('/prediction/')
def prediction():
	global array
	clf=load('modelo_entrenado.pkl')
	array.reshape(1, -1)
	prediccion=clf.predict(array)
	#prediccion=prediccion**10
	prediccion=10**prediccion
	return render_template("prediction.html", args=prediccion)

"""
**App begins its execution**
"""
if __name__ == '__main__':
	app.run(debug=True)