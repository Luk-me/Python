#coding=utf-8
#bubble_sort.py


num=[13,1,8,3,6,5,7,21,9,12,2]
print(num)
for j in range(len(num)):
    for i in range(len(num)-j-1):
        if num[i]>num[i+1]:
            num[i],num[i+1]=num[i+1],num[i]
        else:
            pass
print(num)
   
