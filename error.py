# #syntaxError**
# print("Hello World"
# #NameError**
# if True:
#     x=10
# print(x)
# #TypeError**
# print("Hello World"+1)
# #IndentationError**
# if True:
# print("Hello World")
# #keyError&indexError
# dict1={1:"one",2:"two",3:"three"}
# print(dict1[4])
# list1=[1,2,3]
# print(list1[3])

# #ZeroDivisionError
# print(10/0)

# error handling

# import traceback
# try:
#     print(10/0)
# except ZeroDivisionError:
#     tb = traceback.format_exc()
#     print(tb)
#     print("You can't divide by zero")
# except NameError:
#     print("Name error")
# except Exception as e:
#     print(e)
# finally:
#     print("This will run no matter what")

#raise error
# x=-1
# if x<0:
#     raise Exception("Sorry, no numbers below zero")

