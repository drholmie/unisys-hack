##Representation of the intersections
trends = {
        "j1":{
                        0:(2,1,5,6),
                        1:(1,3,5,6),
                        2:(1,1,2,5),
                        3:(2,4,3,1),
                        4:(3,5,2,1),
                        5:(7,8,6,9),
                        6:(10,12,2,20),
                        7:(68,40,56,20),
                        8:(150,95,89,68),
                        9:(102,69,48,69),
                        10:(80,56,56,68),
                        11:(70,55,42,36),
                        12:(80,68,69,78),
                        13:(126,68,89,65),
                        14:(135,65,78,89),
                        15:(205,98,89,87),
                        16:(150,87,68,68),
                        17:(250,103,45,98),
                        18:(98,85,67,70),
                        19:(65,58,42,29),
                        20:(55,45,36,21),
                        21:(35,15,12,3),
                        22:(25,12,3,6),
                        23:(20,10,3,15)
        },
        "j2":{
                        0:(2,1,5,6),
                        1:(1,3,5,6),
                        2:(1,1,2,5),
                        3:(2,4,3,1),
                        4:(3,5,2,1),
                        5:(7,8,6,9),
                        6:(10,12,2,20),
                        7:(68,40,56,20),
                        8:(150,95,89,68),
                        9:(102,69,48,69),
                        10:(80,56,56,68),
                        11:(70,55,42,36),
                        12:(80,68,69,78),
                        13:(126,68,89,65),
                        14:(135,65,78,89),
                        15:(205,98,89,87),
                        16:(150,87,68,68),
                        17:(250,103,45,98),
                        18:(98,85,67,70),
                        19:(65,58,42,29),
                        20:(55,45,36,21),
                        21:(35,15,12,3),
                        22:(25,12,3,6),
                        23:(20,10,3,15)
        }
}

nice_values = {
        'j1':[0,0,0,0],
        'j2':[0,0,0,0]
}

import pandas
df_j1_1 = pandas.read_csv("./junction1/1.csv")
df_j1_2 = pandas.read_csv("./junction1/2.csv")
df_j1_3 = pandas.read_csv("./junction1/3.csv")
df_j1_4 = pandas.read_csv("./junction1/4.csv")

df_j2_1 = pandas.read_csv("./junction2/1.csv")
df_j2_2 = pandas.read_csv("./junction2/1.csv")
df_j2_3 = pandas.read_csv("./junction2/1.csv")
df_j2_4 = pandas.read_csv("./junction2/1.csv")

final_data = {}
def generate(dataset):
        data = dict()
        count = 0
        for ind in dataset.index: 
                hour = int(dataset["TIMESTAMP"][ind].split('T')[1][:2])
                if (count > 14 and hour == 0):
                        break
                count+=1
                vehicles = int(dataset["vehicleCount"][ind])
                if (hour in data):
                        data[hour] += vehicles
                else:
                        data[hour] = vehicles
        return data

final_data['j1']={
        1:generate(df_j1_1),
        2:generate(df_j1_2),
        3:generate(df_j1_3),
        4:generate(df_j1_4)
}

final_data['j2']={
        1:generate(df_j2_1),
        2:generate(df_j2_2),
        3:generate(df_j2_3),
        4:generate(df_j2_4)
}

print(final_data)
#optimization per hour
junc_list = {0:'j1',1:'j2'}
edge_list = [((0,1),(1,1)),((1,3),(0,3))] #connected lanes

for i in range(24): #for each hour

        for link in edge_list:
                if (final_data[junc_list[link[0][0]]][link[0][1]][i] > 50): #large traffic
                        
                        if (trends[junc_list[link[1][0]]][(i+1)%23][link[1][1]] > 50):
                                #predicted traffic chain, increase nice value in advance to compensate
                                nice_values[junc_list[link[1][0]]][link[1][1]] += 0.2
                        
        print(nice_values,flush=True)
                