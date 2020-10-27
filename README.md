# Deployment-of-Machine-Learning-Model
A demo project to elaborate how a Machine Learning Model is deployed on production using Flask API

## Prerequisites:
Install Scikit Learn, Pandas and Flask (for API).

## Project Structure:
This project consist of:
1. model.py - This contains code for a Machine Learning model to predict employee
salaries based on data in 'hiring.csv' file. ( these data are Experience, Test score and
Interview score )
2. app.py - This contains Flask APIs that receives employee details through computes the
precited value based on our model and returns it.
3. templates - This folder contains the HTML template to allow user to enter employee
detail and displays the predicted employee salary.
4. Static- This folder contains the styling code using CSS

## Running the project:
1. Ensure that you are in the project home directory. Create the machine learning model by
running below command:
'python model.py'
This would create a serialized version of our model into a file model.pkl
2. Run app.py using below command to start Flask API
 'python app.py'
By default, flask will run on port 5000.
3. Navigate to URL [http://localhost:5000]: You should be able to view the homepage
4. Enter valid numerical values in all 3 input boxes and hit Predict to predict the salary
value.
