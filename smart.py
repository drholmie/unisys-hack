import requests
import flask
import json
from flask_cors import CORS
import os
import math
import time
app = flask.Flask(__name__)
CORS(app)

@app.route("/api/v1/routes/pattern", methods = ["POST"])
def patt():
	global dist_arr
	dist_arr.append(flask.request.get_json()['dist'])
	ind=0
	if len(dist_arr) == 4:
		ind=smart_dist()
		dist_arr=[]
	result = dict()
	result['ind'] = ind
	json_sub = json.dumps(result)
	return json_sub

def smart_dist():
	global dist_arr
	import pandas as pd
	from scipy.stats import ks_2samp
	import numpy as np
	data = flask.request.get_json()
	i = 0
	arr_len=0
	samp_arr=[]
	for arr in dist_arr:
		if len(arr)>arr_len:
			arr_len=len(arr)
			samp_arr=arr
	np_arr = samp_arr
	np_arr = np.array(np_arr).flat
	#print(np_arr)
	np_arr_2sampled = []
	np_arr_5sampled = []
	np_arr_10sampled = []
	while i < len(np_arr):
		if i%2 == 0:
			np_arr_2sampled.append(np_arr[i])
		if i%5 == 0:
			np_arr_5sampled.append(np_arr[i])
		if i%10 == 0:
			np_arr_10sampled.append(np_arr[i])
		i+=1
	np_arr_2sampled = np.array(np_arr_2sampled).flat
	np_arr_5sampled = np.array(np_arr_5sampled).flat
	np_arr_10sampled = np.array(np_arr_10sampled).flat
	stat2, p2 = ks_2samp(np_arr,np_arr_2sampled)
	stat5, p5 = ks_2samp(np_arr,np_arr_5sampled)
	stat10, p10 = ks_2samp(np_arr,np_arr_10sampled)
	rule = [p2,p5,p10]
	ind = rule.index(max([p2,p5,p10]))
	return ind

if __name__ == '__main__':
	dist_arr=[]
	app.run(host='0.0.0.0',port=5000)
