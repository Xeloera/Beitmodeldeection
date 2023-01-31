from flask import Flask, request, jsonify,make_response,send_file
from PIL import Image
import requests
import torch
from transformers import BeitFeatureExtractor, BeitForImageClassification
import io 
#import torch
#import torch.nn as nn



app = Flask(__name__)
''' RUN ONCE PER A MACHINE 
feature_extractor = BeitFeatureExtractor.from_pretrained(   #update later for local model
    'microsoft/beit-base-patch16-224-pt22k-ft22k')
model = BeitForImageClassification.from_pretrained(
    'microsoft/beit-base-patch16-224-pt22k-ft22k')

feature_extractor.save_pretrained("./Beit")
model.save_pretrained("./Beit")
'''
feature_extractor = BeitFeatureExtractor.from_pretrained("./Beit")
model = BeitForImageClassification.from_pretrained("./Beit")


model.eval()


@app.route('/predict', methods=['POST'])
def predict():
    image = Image.open(request.files["image"].stream) 
    inputs = feature_extractor(images=image, return_tensors="pt") #classfimifcation 
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_class = model.config.id2label[predicted_class_idx]

    response = make_response(send_file(io.BytesIO(image.tobytes()), #magic
                                       attachment_filename='predicted_image.jpg',
                                       mimetype='image/jpg'))
    response.headers['predicted_class'] = predicted_class
    print(response.headers)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #local networkd
