def myFunction():
    print("This is my first function in Python")

myFunction()

def add():
    print(10+5)
add()

def add2(x,y):
    print(x+y)

add2(5,6)

def add3(x,y):
    return x+y

total = add3(5,3)
print(total)

def displayMsg(name):
    return "Hello "+name

x = displayMsg("Madhu")
print(x)

def displayCountry(country = "India"):
    return "Your country is " + country

print(displayCountry())
print(displayCountry('France'))




