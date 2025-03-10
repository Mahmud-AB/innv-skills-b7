# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def say_hello(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    

# obj_1 = Human("Alice",25)
# print(obj_1.name)
# obj_2 = Human("Bob",30)
# print(obj_2.name)
# # obj_1.say_hello()

class Area:
    
    total_family_count = 0

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.family = []

    def add_family(self, family):
        self.family.append(family)
        self.count += 1
        Area.total_family_count += 1
        print(f"{self.family} has been added to {self.name}")
    
    def count_family(self):
        print(f"{self.name} has {self.count} families")

    def count_area_family(self):
        print(f"{Area.total_family_count} families are living in this area")

building_1 = Area("Building 1")
building_1.add_family("Alice")
building_1.add_family("Bob")
building_1.add_family("Bobi")
building_1.count_family()
print(building_1.__dict__)

building_2 = Area("Building 2")
building_2.add_family("Alice")
building_2.add_family("Bob")
building_2.count_family()
print(building_2.__dict__)
# building_1.count_area_family()
# building_2.count_area_family()
print(Area.total_family_count)
print(building_1.total_family_count)
print(building_2.total_family_count)

