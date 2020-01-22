#coding=utf-8
#bubble_sort.py
import random
num=[]
for i in range(12):
    num.append(random.randint(1,100))

print(num)
for j in range(len(num)):
    for i in range(len(num)-j-1):
        if num[i]>num[i+1]:
            num[i],num[i+1]=num[i+1],num[i]
        else:
            pass
print(num)
   
