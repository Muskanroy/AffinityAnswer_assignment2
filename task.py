# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 09:54:59 2021

@author: muska
"""

from flask import Flask,render_template,request,jsonify
import requests
import pandas as pd
import numpy as np
import csv
import json

app=Flask(__name__)
datapath='C:\\Users\\muska\\OneDrive\\Desktop\\python\\python env\\new\\'

@app.route('/index',methods=['GET','POST'])
def index():   
    return render_template('demo.html')

@app.route('/column',methods=['GET','POST'])
def getColumn ():   
    if request.method == "POST":
        data = pd.read_csv(datapath+'trial.csv')
        column_list=request.form.getlist('column1')
        output=data[column_list].T.to_dict().values()
        output = list(output)
        print(output)
    return render_template('generate_table.html',output=output)
         

if __name__ =='__main__':
    app.run(debug=True)