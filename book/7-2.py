#coding=utf-8
#7-2.py
Boolean=True
while Boolean:
    print('How many people are eating:')
    try:
        num=int(input('>'))
        if num>8:
            print('There are no spare tables.\n')
        elif num<8:
            print('There are spare tables.\n') 
    except:
        Boolean==False

