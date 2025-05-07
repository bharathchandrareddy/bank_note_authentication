from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)  # calling the main function
classifier_in = open('models\classifier.pkl','rb')  # loading the saved model
classifier = pickle.load(classifier_in)   # uloading the pickle file into classifier

@app.route('/')
def welcome():
    return 'welcome all'

@app.route('/predict')
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis= request.args.get('curtosis')
    entropy = request.args.get('entropy')
    predicted_value = classifier.predict([[variance,skewness,curtosis,entropy]])
    return f'the predicted value is = {predicted_value}'
    


if __name__ == '__main__':
    app.run()