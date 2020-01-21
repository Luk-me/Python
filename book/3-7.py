# coding=utf-8

names=['qwe','asd','zxc']

for i in names:
    print("Hello "+i+", welcome to my party")
#print(names.pop(1)+" can't come to party")

names[1]='qaz'

for j in names:
    print("\nHello "+j+", welcome to my party")

print("qweasd..."+'\r\n')

names.insert(0,'poi')
names.insert(2,'wer')
names.append('xcv')

for k in names:
    print("\nHello "+k+", welcome to my party")

print("only two friends.")

while len(names) !=2:
    print("sorry,"+names.pop())

for l in names:
    print("\nHello "+l+",you can come on.")
del names[:]
print(names)
