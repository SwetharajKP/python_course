""" JSON : JavaScript Object Notation
- Data format for storing and exchanging some information
- Every language has libraries for parsing and generating jason data """

""" USE :
- Transfer data/objects from client to server or from type of application to another.
- Used for fetching data from online API's
- in web service"""

""" In python json data is represented as string.
we use json module for this """

""" To convert python to json : 
1. dumps() : does not create file
2. dump() : create a file """

import json
# dict1 = {"name": "swetha", "age": 23, "is_married": False, "insurance": None}
# print(dict1)
# print(type(dict1))
#
# print(json.dumps(dict1))
# print(type(json.dumps(dict1)))

# # array :
# data = ["swetha",23,False,None]
# data1 = ("swetha",23,False,None)
#
# print(json.dumps(data))
# print(type(json.dumps(data)))
#
# print(json.dumps(data1))
# print(type(json.dumps(data1)))

# data = {
#     "Age":23,
#     "City":"kozhikode",
#     "Name":"swetha",
#     "Subject": [
#         "Data Structure",
#         "Computer Graphics",
#         "Discrete mathematics"
#     ],
#     "is_married":False
# }
# print(data)
# print(type(data))

# json_data = json.dumps(data,indent=4,sort_keys=True)
# print(json_data)
# print(type(json_data))
# """ sort_keys=True : sort in alphabetic order """

# # To send to other python application : we will use dump()
# f = open("data.json",mode="w")
# json_data = json.dump(data,f,indent=4,sort_keys=True)
# print(json_data)
# print(type(json_data))

""" To convert json to python :
1. loads() : does not read from file
2. load() : reads json file    """
# data = {
#     "Age":23,
#     "City":"kozhikode",
#     "Name":"swetha",
#     "Subject": [
#         "Data Structure",
#         "Computer Graphics",
#         "Discrete mathematics"
#     ],
#     "is_married":False
# }
# print(data)
# print(type(data))

# json_data = json.dumps(data,indent=4,sort_keys=True)
# print(json_data)
# print(type(json_data))
# # """ sort_keys=True : sort in alphabetic order """

# # Json into python dict :
# data1 = json.loads(json_data)
# print(data1)
# print(type(data1))

# file = open("data.json",mode="r")
# my_data = json.load(file)
# print(my_data)
# print(type(my_data))
# file.close()











































