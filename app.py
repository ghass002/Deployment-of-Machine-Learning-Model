# Import all necessary libraries
import numpy as np
from flask import Flask, request, render_template
import pickle

# Initilize Flask App
app = Flask(__name__)
# load the model in read mode
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """ For rendering results on HTML GUI """
    # extract features from the input in "index.html"
    int_features = [int(x) for x in request.form.values()]
    # convert to an array
    final_features = [np.array(int_features)]
    # predict the value
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)