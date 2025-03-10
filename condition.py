a = 12
# if a == 10:
#     print("a is 10")
# elif a == 1:
#     print("a is 1")
# elif a == 12:
#     print("a is 12")
# else:
#     print("a is not 10")

# if a == 10 and a == 12:
#     print("a is 10")
# elif a == 12:
#     print("a is 1")

#ternary operator
# result if condition else result2 if condition2 else result3
# print("a is 10") if a == 10 else print("a is 12") if a == 12 else print("a is not 10")

#nested if else
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a == 10:
    print("a is 10")
    if b == 12:
        print("b is 12")
    else:
        print("b is not 12")
else:
    if b == 12:
        print("a is 12")
    else:
        print("a is not 12")