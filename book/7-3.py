#coding=utf-8
#7-3.py

while True:
    try:
        num=int(input('Please enter a number.'))
        if num%10==0:   #測試輸入的數能否被10整除
            print('yes')
        else:
            print('no')
    except:
        break
