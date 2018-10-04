fruits = ['apple', 'banana', 'cherry']
print(fruits[0])

fruits[1] = 'orange'
print(fruits)

for x in fruits:
    print(x)

if 'apple' in fruits:
    print('yes')

print('Apple' in fruits)

print(len(fruits))

fruits.append('banana')
print(fruits)

fruits.insert(2, 'pineapple')
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

del fruits[0]
print(fruits)

"""del fruits
print(fruits)"""

"""fruits.clear()
print(fruits) - will work with Python 3"""

colors = list(('apple', 'banana', 'dove', 'cherry'))
print(colors)

colors.reverse()
print(colors)

num = [4, 2, 6, 5, 3, 1]
colors.sort()
print(colors)



