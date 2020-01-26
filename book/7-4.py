# coding=utf-8
# 7-4.py
ingredients = []

while True:
    print('Please enter the ingredients you need.')
    ingredient1 = input('>')
    if ingredient1 == True:
        if ingredient1 == 'exit':
            break
        else:
            print("We will add this ingredient to pizza.")
            ingredients.append(ingredient)
