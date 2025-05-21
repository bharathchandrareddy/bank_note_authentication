from flask import Flask,request, render_template, jsonify
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger   

app = Flask(__name__)  # calling the main function
classifier_in = open('models\classifier.pkl','rb')  # loading the saved model
classifier = pickle.load(classifier_in)   # uloading the pickle file into classifier

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/predict_api')
def predict_note_authentication():
    data = request.json['data']
    print(f'data = ',data)
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis= request.args.get('curtosis')
    entropy = request.args.get('entropy')
    predicted_value = classifier.predict([[variance,skewness,curtosis,entropy]])
    return f'the predicted value is = {predicted_value}'

#render template format. This is approach is slow because its not assynchronus and refreshes the page everytime a call is made
# @app.route('/predict',methods = ['POST'])
# def predict_input():
#     data = [float(x) for x in request.form.values()]
#     predicted_value = classifier.predict([data])
#     return render_template('main.html',predicted_result = 'the predicted class is {}'.format(predicted_value))

@app.route('/predict', methods=['POST'])
def predict_input():
    data = request.get_json()  # Expecting JSON from fetch
    print(f'data = ',data)
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    # Perform prediction
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])[0]

    return jsonify({'prediction': str(prediction)})

if __name__ == '__main__':
    app.run()