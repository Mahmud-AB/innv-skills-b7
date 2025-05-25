# 12345
# structure
# print("1")
# print("2")
# print("3")
# print("4")
# print("5")
# for i in "12345":
#     print(i)
# for i in "12345":
#     print(i)

# for i in range(5):
#     a = 1
#     print(a)

row = 5
#range(start,stop,step)
for i in range(1,row+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")
# for i in range(1,row+1):
#     for j in range(1,row-i+1):
#         print(" ",end=" ")

# row = 5
# for i in range(1,row+1):
#     print(i,end="" if i == row else "\n")
#first step
# i = 1
# 2nd loop
# j start 1 stop 1 + 1 = 2
# range(1,2)
# 1
# seconmd step
# i = 2
# j start 1 stop 2+1 = 3
# range(1,3)
# 1,2
# s="12345"
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1

#break,cotinue,pass

# for i in "12345":
#     if i=="3":
#         break
#     print(i)
# print("=======================")
# for i in "12345":
#     if i=="3":
#         continue
#     print(i)
# print("=======================")
# for i in "12345":
#     if i=="3":
#         pass
# print("=======================")

#list for loop
# list1 = ["apple","banana","cherry"]

# for i in list1:
#     print(i)

# list comprehension
# [assign_value for item in iterable] structure

# list2 = [ a for a in ("apple","banana","cherry") if a!="banana"]
# # list1 = [ b for a in ("apple","banana","cherry") for b in a ]
# list1 = [] 
# for a in ("apple","banana","cherry"):
#     if a!="banana":
#         list1.append(a)
# print("normal",list1)
# print("comprehension",list2)
# list2 = [ x**2 for x in range(5)]
# print(list2)

#enumerate
# list1 = ["apple","banana","cherry"]
# str = "abcd"
# for i,j in enumerate(str):
#     print(i)
#     print(j)
# #zip
# list1 = ["apple","banana","cherry"]
# list2 = ["red","yellow","black"]

# for i,j in zip(list1,list2):
#     print(i,j)
# #tuple
# tuple1 = ("apple","banana","cherry")
# for i in tuple1:
#     print(i)

#dictionary
# dict1 = {"name":"John","age":36}
# for i in dict1.items():
#     print(i)
#     for j in i:
#         print(j)

#dict comprehension
# dict1 = {key:value for value,key in [("name","John"),("age",36)] if key!="name"}
# print(dict1)

#next
# tuple1 = ("apple","banana","cherry")
# print(tuple1)
# print(next(iter(tuple1)))
# print(next(iter(tuple1)))

# tuple1 = (i for i in ("apple","banana","cherry"))
# print(tuple1)
# print(next(tuple1))
# print(next(tuple1))

# j = []
# for i in range(5):
#     j.append(i)
#     print("inside_list",j)
# j.append(i)
# print("outside_list",j)

# rows = 5
# i = 1
# while i<=rows:
#     j = 1
#     stop = rows - i
#     while j<=stop:
#         print(" ",end=" ")     
#         j+=1
#     k = 1
#     while  k<=i:
#         print(k,end=" ")
#         k+=1
#     print("\n")
#     i+=
# # "Write a Program to Identify and Print Perfect Numbers Within a Given Range"
# a=int(input("enter starting value "))
# b=int(input("enter ending value "))
# while a<=b:
#     i=1
#     s=0
#     while i<a:
#         if a%i==0:
#             s=s+i
#         i=i+1
#     if s==a:
#         print(a)
#     a=a+1
# 5-6
# a=5
# i =1
# s=0
# 5%1==0
# s=0+1
# i=2
# 5%2!=0
# i=3
# 5%3!=0
# i=4
# 5%4!=0
# i=5
# 1!=5
# a=6
# i=1
# s=0
# 6%1==0
# s=0+1
# i=2
# 6%2==0
# s=1+2
# i=3
# 6%3==0
# s=3+3
# i=4
# 6%4!=0
# i=5
# 6%5!=0
# i=6
# 6==6
# a=7