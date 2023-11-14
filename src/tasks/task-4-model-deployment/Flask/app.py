from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from numpy import asarray
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np
import PIL
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model

import os

app = Flask(__name__)

dic = {0 : 'Anthracnose',
        1 : 'Bacterial Canker',
        2 : 'Cutting Weevil',
        3 : 'Die Back',
        4 : 'Gall Midge',
        5 : 'Healthy',
        6 : 'Powdery Mildew',
        7 : 'Sooty Mould'}


model = load_model('mango_leaf_disease_ResNet50_archi.h5')

def predict_label(img_path):
	
	img = image.load_img(img_path, target_size=(224,224))
	img_array = image.img_to_array(img)
	img_batch = np.expand_dims(img_array, axis=0)
	
	predictions = model.predict(img_batch)
	label = np.argmax(predictions)
	
	return dic[label]
	


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)
		
		if p == "Healthy":
			image_file_res = "healthy.png"
		else:
			image_file_res = "Unhealthy.png"

	return render_template("index.html", prediction = p, img_path = img_path, image_file_res = image_file_res)


if __name__ == '__main__':
    app.run(debug=True)