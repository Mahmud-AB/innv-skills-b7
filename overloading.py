class Studnet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_id(self, id):
        return f"{self.name} {self.age} {id}"
    
# obj1 = Studnet("Alice", 25)
# print(type(obj1))
# # print(obj1.get_id())
# obj2 = Studnet("Bob", 30)
# # print(obj2.get_id(2))
# print(obj1 + obj2)
# operator overloading
# + __add__
# - __sub__
# * __mul__
# / __truediv__
# // __floordiv__
# % __mod__
# ** __pow__
# == __eq__
# != __ne__
# > __gt__
# < __lt__

class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.img, self.img + other.real)
    
    def __str__(self):
        return f"{self.real} + {self.img}i"
    
number = ComplexNumber(2,3)
print(number)
number2 = ComplexNumber(3,4)
print(number2)
sum = number + number2
other_sum = 2+2
print("sum",sum)
print("other_sum",other_sum)
print(type(sum))
print(type(other_sum))


