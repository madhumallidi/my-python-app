# for conditions

names = ['apple', 'Banana', 'cherry']
for name in names:
    print(name)

msg = 'Hello'
for x in msg:
    print(x)

for name in names:
    print(name)
    if name == 'Banana':
        break

fruits = ['cherry', 'banana', 'apple']
colors = ['red', 'yellow', 'black']

for x in fruits:
    for y in colors:
        print(x, y)
