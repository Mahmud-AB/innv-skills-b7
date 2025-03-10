number = 50

factors = []
divisor = 2

# 12
# 12/1 = 12
# 12/2 = 6
# 6/3 = 2
# 2/4 = 1

while number > 1: # 50 > 1, 25 > 1
    if number % divisor == 0: # 50 % 2 = 0, 25 % 2 != 0
        factors.append(divisor)
        number = number / divisor # 50 / 2 = 25,
    else:
        divisor += 1

print(factors)