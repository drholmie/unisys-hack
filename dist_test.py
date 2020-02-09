import pandas as pd
from scipy.stats import ks_2samp
import numpy as np
df = pd.read_csv("trafficData158324.csv", usecols =["vehicleCount"])
df1 = pd.read_csv("trafficData158355.csv", usecols =["vehicleCount"])
np_arr = df.to_numpy().flat
np_arr1 = df1.to_numpy().flat
#new_sample=[]
#i=0
#while i < len(np_arr):
#	if i%2==0:
#		i+=1
#		continue
#	new_sample.append(np_arr[i])
#	i+=1
#new_sample = np.array(new_sample).flat
print(ks_2samp(np_arr,np_arr1))
