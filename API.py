import flask
import SER_Lib as ser
import librosa as lbr
import os
from os.path import join, abspath, dirname
from flask import request, redirect, session
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def upload_predict():
	if request.method == 'POST':
		file = request.files['file']
		filename = secure_filename(file.filename)
		with open(join(abspath(dirname(__file__)), filename)) as f:
			audio, sampling_rate = lbr.load(join(abspath(dirname(__file__)), filename))
		features = ser.extract_features(audio, sampling_rate)
		try:
			prediction = ser.predict_emotion(features)
			decoded_pred = ser.decode(prediction)
		except Exception as e:
			raise 'Some problem has occurred.'
		session['prediction'] = decoded_pred
	return flask.render_template('home.html')		

@app.route('/json', methods = ['GET', 'POST'])
def json():
	if request.method == 'GET':
		prediction = session.get('prediction', None)
		return flask.jsonify(prediction)
	return 

if __name__ == '__main__':
	app.run(debug = False)