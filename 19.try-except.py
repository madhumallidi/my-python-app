"""try:
    x = 5
    print(x)
except:
    print('error occured')"""

try:
    print(x)
except NameError:
    print('Var x is not defined')
except:
    print('An Error Occured')


try:
    print(x)
except:
    print("Something went wrong")
else:
    print('Nothing went wrong')


try:
    print('Hello')
except:
    print('There is an error')
finally:
    print('The try except is finished')

try:
    f = open('demo.txt')
    f.write('Hello world!')
except:
    print('Something went wrong when writing to file')
finally:
    f.close()

