"""Set is a collection which is unordered and un-indexed
sets are written with curly brackets
it wont allow duplicates"""

thisSet = {'orange', 'red', 'blue', 'black'}

print(thisSet)
print(thisSet)

for x in thisSet:
    print(x)

if 'red' in thisSet:
    print('yes')
else:
    print('no')

thisSet.add('pink')
print(thisSet)

thisSet.update(['pink', 'maroon', 'white'])
print(thisSet)

print(len(thisSet))

thisSet.remove('pink')
print(thisSet)

"""thisSet.remove('pink')
print(thisSet)"""

thisSet.discard('white')
print(thisSet)

# discard will not throw an error
thisSet.discard('white')
print(thisSet)

thisSet.pop()
print(thisSet)

item = thisSet.pop()
print(item)

print(thisSet)

thisSet1 = set(('orange', 'red'))
print(thisSet1)



