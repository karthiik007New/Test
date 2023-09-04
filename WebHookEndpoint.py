#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#added comment 2
"""
Created on Mon Sep  4 09:57:49 2023

@author: karthikj
"""

from flask import Flask, request, jsonify

from flask_cors import CORS  # Import the CORS class
import json


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def WebHook():
    data = request.get_json()
    
    print(data)

    return jsonify(True)




if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True,port=9000)
