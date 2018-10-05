# practice session to write the code of If, For, List

fruits = ['Apple', 'Banana', 'Cherry']

print('Banana' in fruits)
if 'Banana' in fruits:
    print('Yes it is')

for x in fruits:
    print(x)

fruits.append('Orange')
print(fruits)

fruits.insert(2,'Pineapple')
print(fruits)

fruits.remove('Pineapple')
print(fruits)

fruits.pop()
print(fruits)

del fruits[0]
print(fruits)

myTuple = ('SP', 'DP', 'DV', 'FM', 'PM')
print(myTuple)


thisSet = {'banana', 'orange', 'pink'}
print(thisSet)

thisSet.add('yellow')
print(thisSet)

thisSet.update(['white', 'black'])
print(thisSet)

thisSet.remove('banana')
print(thisSet)

thisSet.discard('black')
print(thisSet)

thisSet.discard('black')
print(thisSet)

# thisSet.remove('banana')
# print(thisSet)

item = thisSet.pop()
print(item)
