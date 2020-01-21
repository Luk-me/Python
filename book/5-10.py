#coding=utf-8
#5-10.py

current_users=['qwe','asd','zxc','qaz','wsx']
new_users=['admin','root','qwe','sdf','asd']

for i in new_users:
    i=i.lower()
    for j in current_users:
        j=j.lower()
        if j == i:
            print("Can't create user: "+i)

