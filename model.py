# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

def convert_to_int(word):
	""" Coverts words to integer values """
	word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
				'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
	return word_dict[word]

# load the data
dataset = pd.read_csv('hiring.csv')
# fill tha experience NaN data with 0
dataset['experience'].fillna(0, inplace=True)
# fill the test_score NaN data with the mean
dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)
# Extract the independant variables
X = dataset.iloc[:, :3]
# Convert experience data
X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))
# Extract the dependant variable
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6]]))