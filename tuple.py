t = ('a', 'b', 'c', 'd', 'e','c')
t = dict(t)
print(t)
print(type(t))
# t1 = tuple(('abc','def'))# ('a', 'b', 'c')
# print(type(t1))

print(t[0])
print(t.index('c'))
print(t[:4:2])
print(t.count('a'))

t = list(t)
t.append('f')
t = tuple(t)
prin t(t)

t = list(t)
t.remove('f')
t = tuple(t)
print(t)

t1 = ('z',)

t = t + t1

print(t)

# t += t1 * 2

t2 = t1 * 2
print(t2)

t = t + t2

print(t)

# del t1


# t = ('a', 'b', 'c')

# (t1, t2, t3)= t
# print(t1)
# print(t2)
# print(t3)

(t1, t2, *t3) = t

print(t1)
print(t2)
print(t3)