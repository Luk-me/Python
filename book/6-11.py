#coding=utf-8
#6-11.py

cities={
    'New York':{
        'countries':'US',
        'population':'10000',
        },
    'Beijing':{
        'countries':'China',
        'population':'1400000000'
        },
    'London':{
        'countries':'UK',
        'population':'100000',
        },
    }

for city,information in cities.items():
    print('\n'+city+':')
    print('\tcountries:'+information['countries'])
    print('\tpopulation:'+information['population'])


