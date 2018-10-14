# Dictionary
# Which is unordered, changeable, no duplicates are allowed
"""
theDict = {
    "firstname": "Madhu",
    "Lastname": "Mallidi",
    "city": "Hyderabad",
    "user": {
        "firstname": "Manasvi",
        "lastname": "Mallidi",
        "city": "Hyderabad"
    }
}
print(theDict)

firstname = theDict["firstname"]
print(firstname)

lastname = theDict.get("Lastname")
print(lastname)

firstname2 = theDict.get("user")
print(firstname2.get("firstname"))


theDict1 = {
    "user1": ["john", "Mark", "Joe"],
    "city": ["Paris", "Singapore", "Swiss"]
}

userlist = theDict1.get("user1")
print(userlist[0])

theDict["firstname"] = "madhukumar"
print(theDict)

for x in theDict:
    print(x)

for x in theDict:
    print(theDict[x])

for x in theDict1.values():
    print(x)

for x,y in theDict1.items():
    print(x,y)

if "firstname" in theDict:
    print("first name in s in the Dictionary")

print(len(theDict))

theDict["state"] = "TS"
theDict["Country"] = "India"

print(theDict)

del theDict["state"]
print(theDict)

if "state" in theDict:
    print("Yes")
else:
    print("no")

theDict.pop("Country")
print(theDict)

theDict.popitem() # removes the last inserted item in Python 3. In version before phython 3, random items are removed
print(theDict)

del theDict
print(theDict)

theDict.clear()
print(theDict)
"""
dict = dict(city = "paris", firstname = "John", lastname = "mark")
print(dict)

#for key, values in theDict.items():
#   print(key, values)
#for key in theDict:
#    print(key)

print(dict.keys())

for key in dict:
    print(key)

for key, value in dict.items():
    print(key,value)


