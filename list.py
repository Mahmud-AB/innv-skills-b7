
## int float str bool list tuple dict set

# # int
# a = 10
# print(a)
# print(type(a))

# # float
# b = 10.4
# print(b)
# print(type(b))

# # str
# print(type("hello world"))

# # bool
# is_true = False
# print(type(is_true))

# list
# list1 = [1, 2, 3, 4, 5]
# print(len(list1))
# print(list1.count(1))
# print(list1[0])
# print(type(list1))

# list3 = list1
# print(list3)
# print(list1)
# list3.append(50)
# print(list3)
# print(list1)

# # dict
# dict1 = {
#         "key" : "value",
#         "name": "zhangsan", 
#         "age": 18
#         }
# print(dict1["name"])
# print(type(dict1))

# # tuple
# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1[0])
# print(type(tuple1))
# # set
# set1 = {1, 2, 3, 4, 5}
# print(type(set1))

#constructor
# n = (7, 8, 11, 9, 10)
# print(n)
# print(type(n))
# list2 = list(n)
# print(type(list2))

# list1 = [1, 2, 3, 4, 5]

# print("list",list1)

# #access
# print("value",list1[0])

# print("index_number",list1.index(3))

# print(list1[:4:2])

# print(list1[-1::-1])

# #add
# list1.append(6)
# print("append",list1)
# list1.insert(0,0)
# print("insert",list1)
# list1.extend(list2)
# print("extend",list1)

##remove
# pop_value = list1.pop(6)
# print("pop_value",pop_value)
# print("pop",list1)
# a = list1.remove(0)
# print(a)
# print("remove",list1)
# del list1[0]
# print("del",list1)
# list1.clear()
# print("clear",list1)

#loop
# for i in list2:
#     print(i)
# list3 = list2
# print(list3)
# print(list2)
# list3.append(50)
# print(list3)
# print(list2)

# list3 = [3,2,6,1,5,4]
# list2 = list3.copy()
# list2.append(50)
# print(list2)
# print(list3)
# list3.sort(reverse=True)
# print("sort",list3)
# list3.sort()
# list3.reverse()
# print("reverse",list3)
# print("list2",list2)
# list2.reverse()
# print("reverse",list2)



# l1 = [1, 2, 3, 4, 5]
# l2 = [3,4,5,6,7]

# if not l2 in l1:
#     print("not found")
#     l2.append(l1)
# print(l2)
    
#slice
# [start:stop:step]
# initial start 0 index
# initial start for reverse -1 index
# initial stop last index/n-1, n = length of list
# initial stop for reverse 0 index
# initial step 1

# list1= [1,2,3,4,5]
# print(list1[2:4])
#for list 1 
# index number    reverse index number
#   0   1                   -1  5
#   1   2                   -2  4
#   2   3                   -3  3
#   3   4                   -4  2
#   4   5                   -5  1

# list1[:-2]
# print(list1[:-2])

# list1[::-1]    # all items in the array, reversed

# list1[-2:]
# print(list1[-2:])
# print(list1[-3:]

# list1= [1,2,3,4,5]
# list1[-1:-4:-1]
# print(list1[-1:-4:-1])
# list1[1::-1]   # the first two items, reversed
# print(list1[1::-1])
# list1[:-3:-1]  # the last two items, reversed
# print(list1[:-3:-1])
# list1[-3::-1]  # everything except the last two items, reversed
# print(list1[-3::-1])


