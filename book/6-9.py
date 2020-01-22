#coding=utf-8
#6-9.py

favorite_places={
    'Lusky':['qwe','asd','zxc'],
    'lusky':['qaz','wsx','edc'],
    'LUSKY':['qsc','wdv','efv'],
    }
for name,places in favorite_places.items():
    print('\n'+name+"'s favorite places is: ")
    for i in places:
        print(i)
