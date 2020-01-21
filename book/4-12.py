#coding=utf-8
#foods.py

my_foods=['pizza','falafel','carrot cake']
friends=my_foods[:]
my_foods.append('apple')
friends.insert(1,'cookie')
print("My favourite foods are:")
for i in my_foods:
    print(i)
print("\nmy friends favourite foods are:")
for j in friends:
    print(j)

