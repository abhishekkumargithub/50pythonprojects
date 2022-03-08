#for loop
numbers=[1,2,3]
new_list=[]
for n in numbers:
    add_1=n+1
    new_list.append(add_1)

#List Comprehension

new_list=[n+1 for n in numbers]

#String as list
name="Angela"
letters_list=[letter for letter in name]

#range as list
range_list=[num*2 for num in range(1,5)]

#Conditional list Comprehension
names=["Alex","Berth","Caroline"]

