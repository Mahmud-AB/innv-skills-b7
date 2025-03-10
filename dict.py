
dict1 = {
    "name":"john",
    "age":23,
    "address" : "USA"
}
print(type(dict1))
print(dict1.values())
print(dict1.keys())
print(dict1["age"])
print(dict1.get("name"))

print(dict1.items())

dict1["age"] = 24

print(dict1)

# dict1["roll"] = 101
# print(dict1)

dict1.update({
    "roll":101
    }
    )



# name  = dict1.pop("name")
# print(name)
# print(dict1)
roll = dict1.popitem()

print(roll)
print(dict1)

# dict1.clear()
# print(dict1)

# del dict1
# print(dict1)

# dict1 = {
    
# }
print(len(dict1))