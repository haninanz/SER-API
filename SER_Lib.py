import numpy as np
import librosa as lbr
import tensorflow as tf
from keras import models
from tensorflow.compat.v1 import disable_v2_behavior, placeholder, Session

def extract_features(audio_file, sampling_rate = 16000):
	"""
	Return extracted features (MFCC, Contrast, and Tonnetz) from the input mono-channel .wav audio.

	Keyword arguments: 
	audio_file -- The uploaded audio to be predicted.

	sampling_rate -- The sampling rate of audio_file. Default value is 16000 Hz.
	"""
	transformed = np.abs(lbr.stft(audio_file))
	mfcc = np.mean(lbr.feature.mfcc(y = audio_file, sr = sampling_rate, n_mfcc = 40).T, axis = 0)
	cont = np.mean(lbr.feature.spectral_contrast(S = transformed, sr = sampling_rate).T, axis = 0)
	tonn = np.mean(lbr.feature.tonnetz(y = lbr.effects.harmonic(audio_file), sr = sampling_rate).T, axis = 0)
	ext_features = np.hstack([mfcc, cont, tonn])
	return ext_features.reshape((1, 1, ext_features.shape[0]))

def predict_emotion(input_file):
	"""
	Return the predicted emotion of an extracted audio.

	Keyword arguments:
	input_file -- Extracted features of an audio.
	"""
	model = models.load_model('model_ser.h5')
	predictions = model.predict(input_file)
	results = np.array([np.argmax(prediction) for prediction in predictions])
	return results

def decode(prediction):
	"""
	Return the decoded emotion from the prediction.

	Keyword arguments:
	prediction -- the result prediction from the model.
	"""
	emotion_dict = {'Neutral': 0, 'Angry': 1, 'Sad': 2, 'Happy': 3}
	for emotion, code in emotion_dict.items():
		if prediction == code:
			return emotion

