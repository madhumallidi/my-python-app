myTupple = ('apple', 'banana', 'cherry')
print(myTupple)

print(myTupple[1])
# myTupple[1] = 'Orange' - doesnt work in Tupple

for x in myTupple:
    print(x)

if 'banana' in myTupple:
    print('yes')

print(len(myTupple))

"""del myTupple
print(myTupple)"""

colors = tuple(("red", "black", "blue" ))
print(colors)
