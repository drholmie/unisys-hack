# import requests
# import flask
# import json
# from flask_cors import CORS
# from tinyec.ec import Curve, SubGroup
# import secrets
import pandas as pd
import numpy as np
import math
# app = flask.Flask(__name__)
# CORS(app)

def print_status():
    for i in street_arr:
        print("Status: ",i.status, "Count: ", i.static_count)

    
    
class street:
    def __init__(self, index, status, rule, data):
        self.status = status
        self.index = index
        self.rule = rule
        self.data = data
        self.del_index = []
        self.static_count = 0 
    def count(self, time):
        sum = 0 
        i = 0
        while i <= int(time/5) and i < len(self.data):
            sum += self.data[i]
            self.del_index.append(i)
            i += 1
        return sum
    def delete(self, val):
        if val == 0:
            self.del_index = []
        else:
            self.data = np.delete( self.data, self.del_index)
            #print(self.del_index)
            self.del_index = []

def timer(rule):
    math.floor(rule)
    rule = rule if rule/10 == 0 else (rule-(rule%10))
    time.sleep(rule-10)
    brain(rule)


def hardlimit(limit):
    global street_arr
    min = 1000000
    count = 0
    min_index = 0 
    time_arr = dict()
    for i in street_arr:
        c=0
        sum = i.static_count
        if i.status != "red":
            continue
        while sum < limit and c < len(i.data):
            sum+=i.data[c]
            c+=1
        time_arr[i.index] = [sum, c*5]
    #print(time_arr)
    for count in time_arr.keys():
        if min > time_arr[count][1]:
            min = time_arr[count][1]
            min_index = count
    return time_arr[min_index][1]

def brain(time):
    #assumption when green every vehicle counted goes through and count resets to 0
    #for that signal
    global street_arr
    max = -1
    i = 0
    max_street = 0
    time = hardlimit(100) if hardlimit(100) < time else time
    print("at T=",time)
    while i < len(street_arr):
        if street_arr[i].status != "red":
            street_arr[i].count(time)
            street_arr[i].delete(time)
            street_arr[i].static_count = street_arr[i].data[0]
            street_arr[i].status = "red"
            i += 1
            continue
        street_arr[i].static_count += street_arr[i].count(time)
        street_arr[i].delete(time)
        if max < street_arr[i].static_count:
            max = street_arr[i].static_count
            max_street = i
        i+=1
    street_arr[max_street].status = "green"

street1 = street(0, "red", 60, pd.read_csv("trafficData158324.csv", 
                    usecols =["vehicleCount"]).to_numpy().flat)
street2 = street(1, "red", 60, pd.read_csv("trafficData158355.csv", 
                    usecols =["vehicleCount"]).to_numpy().flat)
street3 = street(2, "red", 60, pd.read_csv("trafficData158386.csv", 
                    usecols =["vehicleCount"]).to_numpy().flat)
street4 = street(3, "red", 60, pd.read_csv("trafficData158415.csv", 
                    usecols =["vehicleCount"]).to_numpy().flat)
street_arr = [street1,street2,street3,street4]

brain(0)
print_status()

brain(60)
print_status()

brain(60)
print_status()

brain(60)
print_status()

brain(60)
print_status()

# def counter():
#     start = time.time()

# #server side event
# @app.route("/api/v1/routes/decision")
# def decision():
#     pass
# @app.route("/api/v1/routes/count")
# def count():
#     global traffic_arr
#     global sleep
#     time.sleep(sleep)
#     pass

# def brain(time):
#     global street_arr
#     max = -1
#     i = 0
#     max_street = 0
#     while i < len(street_arr):
#         count = street_arr[i].count(time)
#         if max < count:
#             max = count
#             max_street = i
#         i+=1
#     street_arr[i].status = "green"

# if __name__ == '__main__':
#     street1 = street("red", 60, pd.read_csv("trafficData158324.csv", 
#                       usecols =["vehicleCount"]).to_numpy().flat)
#     street2 = street("red", 60, pd.read_csv("trafficData158355.csv", 
#                       usecols =["vehicleCount"]).flat)
#     street3 = street("red", 60, pd.read_csv("trafficData158386.csv", 
#                       usecols =["vehicleCount"]).flat)
#     street4 = street("red", 60, pd.read_csv("trafficData158415.csv", 
#                       usecols =["vehicleCount"]).flat)
#     street_arr = [street1,street2,street3,street4]
#     app.run(host='0.0.0.0',port=8085)