#coding=utf-8
#quick_sort.py

import random

num=[]
for i in range(12):
    num.append(random.randint(1,100))
print(num)

def quick_sort(num):
    left=[]
    right=[]
    mid=[]
    if len(num) <=1:
        return num
    for i in num:
        pivot=num[0]
        if i==pivot:
            mid.append(i)
        elif i<pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left)+mid+quick_sort(right)

print(quick_sort(num))