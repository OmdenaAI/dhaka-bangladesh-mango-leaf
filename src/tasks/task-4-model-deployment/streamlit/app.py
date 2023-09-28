import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from PIL import Image

st.image('images/omdena-logo.png', width=100)
st.markdown('<h2 style="color:black;">Mango Leaf Disease Classification Web App</h2>', unsafe_allow_html=True)
st.markdown('<h3 style="color:gray;">This app predicts the disease in mango leaves</h3>', unsafe_allow_html=True)

img_height = 224
img_width = 224

model = Sequential()
model.add(ResNet50(include_top=False, pooling='max', weights= 'imagenet'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(8))
model.layers[0].trainable = False
model.compile(Adam(learning_rate=0.001), loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

# Load the model
model.load_weights('model/mango_leaf_classification_model_weights_omdena_resnet50.hdf5')

upload= st.file_uploader('Upload the image of mango leaf for disease detection', type=["png", "jpg", "jpeg"])
c1, c2= st.columns(2)
c1.header('Uploaded Image')
c2.header('Predicted Class')

classes = [ 'Anthracnose',
            'Bacterial Canker',
            'Cutting Weevil',
            'Die Back',
            'Gall Midge',
            'Healthy',
            'Powdery Mildew',
            'Sooty Mould']

if upload is not None:
    img = Image.open(upload)
    img = img.resize((img_height, img_width))
    img = img.convert("RGB")
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    prediction = model.predict(img)
    img = load_img(upload, target_size=(img_width,img_height))
    c1.image(img)
    c2.write(f'{classes[np.argmax(prediction)]}')

