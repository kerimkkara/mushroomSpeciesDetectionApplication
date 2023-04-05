import os
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model('model.h5')

def closest_to_one(arr):
   arr = np.array(arr)
   idx = (np.abs(arr - 1)).argmin()
   distance = abs(arr[idx] - 1)
   return (arr[idx], distance, idx)

@app.route('/api', methods=['POST'])
def predict():
    # Get the image from the POST request
    file = request.files['image']
    # Save the image to a temporary file
    filename = 'tmp.jpg'
    file.save(filename)
    # Load the image with Keras
    img = load_img(filename, target_size=(400, 350))
    # Preprocess the image
    img = np.array(img) / 255.0
    img = img.reshape(1, 400, 350, 3)
    # Make the prediction with the model
    val = model.predict(img)
    # Process the prediction result
    liste = []
    a_list = list(val)
    for item in a_list:
        for item2 in item:
            liste.append(item2)
    liste2 = closest_to_one(liste)
    index = liste2[1]
    if liste2[2] == -1 or liste2[1] > 0.5:
        tur = "Tespit edilemedi"
    else:
        index = liste2[2]
        if(index == 0):
            tur = 'Amanita_albidostipes'
        elif(index == 1):
            tur = 'Amanita_fritillaria'
        elif(index == 2):
            tur = 'Atractosporocybe_inornata'
        elif(index == 3):
            tur = 'Boletus_erythropus'
        elif(index == 4):
            tur = 'Gomphidius_roseus'
        elif(index == 5):
            tur = 'Hydnum_repandum'
        elif(index == 6):
            tur = 'Russula_rosea'
        else:
            tur = "Tespit edilemedi"
    # Return the prediction result as a JSON response
    return jsonify({'result': tur})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
