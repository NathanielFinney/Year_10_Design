# What is a list?

# A list consists of comma-seperated values(elements) between square brackets.

# Indexed by zero.

# List entries (elements) can be in different types.

import json

myList = [2, 5, "lion", 8, 42, 33]

isInList = 7 in myList
print(isInList)

myList = myList + [21, 56]

# Python is the only language that can concatonate lists.

print (myList)

for n in myList:
    print (n)

for n in range(0, 3):
    print(myList[n])

#print (max(myList))

# Find out where something is in a list

if 100 in myList:
    print (myList.index(100))
else:
    print ("Not found")

# Find the last entered number for a list

print (myList.pop())

# Dictionaries

# A dictionary consists of key:value pairs, seperated by commas and contained in brace brackets {}

# Indexed on the key names

# Keys must be unique

# The leongth of a dictionary is the number key:value pairs it contains

myDictionary = {'id':'001', 'name':'Superman', 'power':'X-Ray Vision'}

superhero = myDictionary['name']

print (superhero)

# JSON Strings

JString = '{"name":"Felix", "age":20, "city":"Toronto"}'

data = json.loads(jString)

print(data["city"])

jString = '[{"name":{"firstName":"Cleopatra", "lastName" : "Ptolemy"}, "address": {"city":"Alexandria", "province":"Egypt"}}, {"name":{"firstName":"Marc", "lastName":"Antony"}, "address":{"city":"Rome", "province":"Italia"}}]’

# the 1 is the second part of the string (0 is the start in computing)
print(data[1]["address"]["city"])