from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# About Page
@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')

# Dataset Page
@app.route('/database', methods=['POST', 'GET'])
def dataset():
    return render_template('dataset.html')

# Visualization Page
@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

# Input Prediction Page
@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    return render_template('predict.html')

# Prediction Result Page
@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form

        df_predict = pd.DataFrame({
            'age':[input['age']],
            'job':[input['job']],
            'marital':[input['marital']],
            'education':[input['education']],
            'default':[input['default']],
            'balance':[input['balance']],
            'housing':[input['housing']],
            'loan':[input['loan']],
            'contact':[input['contact']],
            'day':[input['day']],
            'month':[input['month']],
            'campaign':[input['campaign']],
            'pdays':[input['pdays']],
            'previous':[input['previous']],
            'poutcome':[input['poutcome']]
        })

        prediksi = model.predict_proba(df_predict)[0][1]

        if prediksi > 0.5:
            subscribe = "SUBSCRIBE"
        else:
            subscribe = "NOT SUBSCRIBE"

        return render_template('result.html',
            data=input, pred=subscribe)

if __name__ == '__main__':
    filename = 'D:/Purwadhika/Final Project/Dashboard Bank/Bank_Model.sav'
    model = pickle.load(open(filename, 'rb'))
    app.run(debug=True)