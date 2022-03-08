'''
with open("/100days of python/day25/weather_data.csv") as data_file:
    data=data_file.readlines()
    print(data)

import csv
with open("/100days of python/day25/weather_data.csv") as data_file:
    data=csv.reader(data_file)
    temperatures=[]
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)

import pandas
data = pandas.read_csv("/100days of python/day25/weather_data.csv")
#print(type(data))
#print(data["temp"])

#data_dict=data.to_dict()
#print(data_dict)

temp_list=data["temp"].to_list()
print(len(temp_list))

#sum(temp_list/len(temp_list))
print(data["temp"].mean())
print(data["temp"].max())

#get data in columns
print(data["Condition"])
print(data.Condition)
'''

#get data in row
#print(data[data.day=="Monday"])
#print(data[data.temp==data.temp.max()])
'''
monday=data[data.day=="Monday"]
monday_temp=int(monday.temp)
monday_temp=9/5 +32
print(monday_temp)

 #create adataframe from scratch
data_dict={
    "student":["Any", "James", "Angela"],
    "scores":[76, 56, 65]
}
data= pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
'''
import pandas
data=pandas.read_csv("/100days of python/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Colors"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Colors"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Colors"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict={
    "Fur color":["Grey","Cinnamon","Black"],
    "Count":[grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df= pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")






