#coding=utf-8

#5-6.py

def check(age):
    if age<2:
        print("x<2")
    elif age>=2 and age<4:
        print("2<=x<4")
    elif age>=4 and age<13:
        print("4<=x<13")
    elif age>=13 and age<20:
        print("13<=x<20")
    elif age>=20 and age<65:
        print("20<=x<65")
    else:
        print("x>=65")


age=int(input(">"))
check(age)
