
from wsgiref import  simple_server
from flask import Flask, request, render_template, redirect, url_for
from flask import Response
import os
from flask_cors import  CORS,cross_origin
import flask_monitoringdashboard as dashboard
import pandas as pd
import mysql.connector
from MLprediction import prediction
import json

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app=Flask(__name__)
app.config['DEBUG']=True
dashboard.bind(app)
CORS(app)

app.config
['DEBUG']==True

@app.route("/")
@cross_origin()
def home():
    return render_template('index.html')
#Uploading the Files
UPLOAD_FOLDER='CSV Files'
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

# Uploading the file and building Model & predicting
@app.route("/",methods=['POST'])
def uploadfiles():
    uploaded_file=request.files['file']
    if uploaded_file.filename!='':
        uploaded_file_path=os.path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename)
        uploaded_file.save(uploaded_file_path)
    pred_obj=prediction(uploaded_file_path) # Object Initialization for prediction
    output=pred_obj.fnprediction() # Calling fnprediction
    return Response('Prediction file created at'+str(uploaded_file_path)+'and few of the predictions are'+str(json.loads(output)))






if (__name__ == "__main__"):
     app.run(port = 8000)








