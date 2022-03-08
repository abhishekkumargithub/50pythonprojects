student_dict={
    "student":["Angela","James","Lilly"],
    "score":[56, 76,98]
}

#Looping throungh dictionaries:
#For (key,value) in student-dict.items():
#prnt(value)
import pandas 
student_data_frame=pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
#for(key,Value) in student_data_frame.items():
#  print(Value)

#Loop through rows of data frame
for(index,row) in student_data_frame.iterrows():
    #print(row.student)
    if row.student=="Angela":
        print(row.score)
        

