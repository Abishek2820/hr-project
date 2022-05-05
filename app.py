#Importing required Libraries
#flask for API development
from flask import Flask, request, render_template
#pickle for reading .pkl file
import pickle
#numpy for array
import numpy as np



#reading .pkl file
path='dpp.pkl'
model = pickle.load(open(path, 'rb'))

#creating instance for Flask 
app=Flask(__name__)


#getting input from frontend
@app.route('/input',methods=['GET','POST'])
def input():
    details=request.form
    #getting carat, cut, color, clarity, depth and table as input to predict diamond price
    #carat= float(details['carat'])
    sl=int(details['sl'])
    le=int(details['le'])
    np=int(details['np'])
    am=int(details['am'])
    ts=int(details['ts'])
    wa=int(details['wa'])
    pl=int(details['pl'])
    dp=int(details['dp'])
    sa=int(details['sa'])
    #passing values as numpy array and predicting the price in dollar
    prediction=model.predict([[sl,le,np,am,ts,wa,pl,dp,sa ]])
    #converting dollar to INR using web scraped data
    msg=''
    if prediction[0]==1:
        msg=msg+'left the company'
    else:
        msg=msg+'Not left the company'
    print(msg)
    #rendering price to output page
    return render_template('output.html', msg=msg)

#rendering to input page
@app.route('/')
def submit():
    return render_template('input.html')
#main function
if __name__ == '__main__':
    app.run(debug=True)