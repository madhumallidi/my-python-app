import json

obj = '{"name": "John", "city": "HYD", "state": "TS"}'
print(obj)
# to change this to dictionary, use Json.loads()
myDict = json.loads(obj)
print(myDict)

myJson = json.dumps(myDict)
print(myJson)

# convert into JSON
print(json.dumps(['A', 'B', 'C']))
print(json.dumps('Hello world!'))
print(json.dumps(None))







