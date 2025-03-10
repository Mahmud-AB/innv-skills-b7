# print("hello")
# len()
# type()

# # function structure
# def function_name(param):
#     statement
#     pass
# # function call
# function_name(argument)
# function_name(argument)

# g = "global" #global variable
# def my_function():
#     print(g)
#     l = "local" #local variable
#     print("Hello from function")
#     return "Hello from a Return"

# var = my_function()
# print(var)

# # arg = "argument"
# def my_function(*arg):
#     print(type(arg))
#     return sum(arg)

# var = my_function(15,25,35,45,55)
# print(var)

# # kwargs = "keyword argument"
# def my_function(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
#     return kwargs

# var = my_function(name="John",age=36)
# print(var)

# def my_function(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     return args,kwargs

# var = my_function(15,25,35,45,55,name="John",age=36)
# print(var)


# def my_function(a,b,c=0):
#     my_function(15,25,35)
#     return a+b+c

# var = my_function(15,25,35)
# print(var)
# var1 = my_function(15,25)
# print(var1)


#lambda function
#structure
# lambda argument_list : expression
# sum = lambda a,b,c : a+b
# sum = lambda *args: sum(args)
# sum_lambda = lambda *args,**kwargs: (sum(args),kwargs)
# print(sum_lambda(5,10,a=5,b=10))

#decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Something is happening before the function is called.")

#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print(f"Hello {name}")

# say_hello("John")
# say_hello = my_decorator(say_hello)

# def log_time(func):
#     print("Decorator is called")
#     def wrapper(*args,**kwargs):
#         print(f"Function {args} is called")
#         result = func(*args,**kwargs)
#         print(f"Function {args} is finished")
#         return wrapper
#     print(wrapper)
#     print("Wrapper is returned")
#     print("=====================================")
#     return wrapper

# @log_time
# def multiply(a,b):
#     print(a*b)

# multiply(5,10)
# print("=====================================")
# multi = log_time(multiply(5,10))
# print(multi)

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("")
#         func(*args,**kwargs)
#     return wrapper

# @decorator
# def check_time(name):
#     print("Checking")
#     print(f"{name} Entered")

# check_time("John")
# check_time("John1")

#recursion
 #base case, recursive case
# 5! = 5*4*3*2*1 
# 5! = 5*4! 
# 4! = 4*3!  #recursive case
# 3! = 3*2!
# 2! = 2*1!

# 1! = 1  #base case

# 5 = n
# n
# (n-1)!
# def factorial(n):
#     print('n',n)
#     print('n-1',n-1)
#     print("==========")
#     if n == 2:
#         return 2
#     else: 
#         return n * factorial(n-1)
#             #   5 * factorial(4)
#             #         4 * factorial(3)
#             #               3 * factorial(2)
#             #                     2 * factorial(1)
#             #                           1
# print(factorial(5))
# 0,1,1,2,3,5,8

# 0 0
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
# 6 8

# 0 n
# 1 n+1
# 1
# 2
# 3
# 5
# 8
#  0 1
# N =0 0
# N =1 1
#  6TH
# (6-1) + (6-2)

# [1,3,5,7,9]
# 1
# 3
# 5
# 7
# 9
# def sum_list(l):
#     if len(l) == 1:
#         return l[0]
#     else:
#         return l[0] + sum_list(l[1:])
    
    # 1 + sum_list([3,5,7,9])
    #     3 + sum_list([5,7,9])
    #         5 + sum_list([7,9])
    #             7 + sum_list([9])
    #                 9
# print(sum_list([5,3,5,7,9]))

# map

# map(function,iterable)

# words = ['apple','banana','cherry']

# def find_length(word):
#     return len(word)

# print(find_length('apple'))
# print(find_length('banana'))
# print(tuple(map(lambda word: len(word), words)))
# print(list(map(find_length,words)))
# print([len(word) for word in words])

#any,all
# numbers = [6,7,8,9,10]
# result = any(numbers>5 for numbers in numbers)
# print(result)
# result = all(numbers>5 for numbers in numbers)
# print(result)
# print(any([True,False,False]))
# print(all([True,False,True]))

#filter
# numbers = [1,2,3,4,5,6,7,8,9,10]
# result = filter(lambda x:x>5,numbers)
# print(list(result))

#enumerate
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for index,number in enumerate(numbers):
#     print(index,number)

#zip,min,max,sum,reduce


# name1 = "      hello world       "
# # print(name1)
# name1.strip()
# print(name1)
# print(name1.strip())

# name2 = name1.replace("hello", "hi")
# print(name2)

# name1 = "hello world tony"

# name1= name1.split(" ")