# O(1) - constant time
# logn - logarithmic time
# n - linear time
# nlogn - log-linear time
# n^2 - quadratic time
# 2^n - exponential time

# #constant time
# n = 1
# print(n) # 1 

# #linear time
# for i in range(2):
#     print(i) # 2 

# #quadratic time,cubic time,....
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(i, j, k) #n^3 cubic time
#         print(i, j) # 4 quadratic time

#logarithmic time
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# left = 0
# right = len(l) - 1
# f = 5
# count = 0
# while left <= right:
#     count+=1
#     print("count",count)
#     mid = (left + right) // 2
#     if l[mid] == f:
#         print(mid)
#         break
#     elif l[mid] < f:
#         left = mid + 1
#     else:
#         right = mid - 1

# #log-linear time
# [4,8,3,7,2,6,1,5]

# [4,8,3,7], [2,6,1,5]

# [4,8], [3,7], [2,6], [1,5]

# [4], [8], [3], [7], [2], [6], [1], [5]

# [4,8], [3,7], [2,6], [1,5]

# [3,4,7,8], [1,2,5,6]

# [1,2,3,4,5,6,7,8]

# exponential time
# recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) # 2^n

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#space complexity
# O(1) - constant space
# O(n) - linear space
# O(n^2) - quadratic space
# O(logn) - logarithmic space
# O(nlogn) - log-linear space
# O(2^n) - exponential space

#constant space
# n = 10
# print(n)

# #linear space
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l)

# #quadratic space
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# #logarithmic space
#where n is the number of elements in the list
#and space reduces proportinaly in each iteration
#binary search

# #log-linear space
# #merge sort
# Divide logn
# Conquer n
# Combine nlogn

# #exponential space
# #recursion