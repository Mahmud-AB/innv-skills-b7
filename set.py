s = {"a", "b", "c"}
# set({"a", "b", "c"})

s.add("d")
print(s)

s1 = ["e", "f", "g","a"]

s.update(s1)

print(s)

# list1 = ["a", "b", "c", "d", "e", "f", "g","a","b","c","d","e","f","g"]
# s = set(list1)
# list1 = list(s)
# print(list1)

s.remove("a")
print(s)
s.discard("b")
print(s)
s.pop()
s.clear()
del s

s2 = {"b", "d", "e"}
s = {"a", "b", "c"}
s3 = s.union(s2)
print(s3)
s4 = s.intersection(s2)
print(s4)
s5 = s.difference(s2)
print(s5)
s6 = s.symmetric_difference(s2)
print(s6)
print(len(s))