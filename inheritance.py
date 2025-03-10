# # single inheritance
# class Parent:
#     def __init__(self):
#         print("Parent class constructor")

#     def parent_method(self):
#         print("Parent method")

# class Child(Parent):
#     def __init__(self):
#         print("Child class constructor")

#     def child_method(self):
#         print("Child method")

# # Create an object of Child class
# child = Child()
# child.child_method()
# child.parent_method()

# parent = Parent()
# parent.parent_method()
# parent.child_method() # AttributeError: 'Parent' object has no attribute 'child_method'

# #mulpiple inheritance
# class Flyable:
#     def fly(self):
#         print("Flying")
    
# class Swimmable:
#     def swim(self):
#         print("Swimming")

# class Duck(Flyable, Swimmable):
#     pass

# duck = Duck()
# duck.fly()
# duck.swim()

# # Multilevel inheritance
# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     class Animal:
#         def eat(self):
#             print("Eating")
#     def bark(self):
#         print("Barking")

# class BabyDog(Dog):
#     def weep(self):
#         print("Weeping")

# baby_dog = BabyDog()
# baby_dog.eat()
# baby_dog.bark()
# baby_dog.weep()

# dog = Dog()
# dog.eat()

# # Hierarchical inheritance
# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def bark(self):
#         print("Barking")

# class Cat(Animal):
#     def meow(self):
#         print("Meowing")

# dog = Dog()
# dog.eat()
# dog.bark()
# cat = Cat()
# cat.eat()
# cat.meow()

# # Hybrid inheritance
# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def bark(self):
#         print("Barking")

# class germanShepherd(Dog, Animal):
#     def color(self):
#         print("Black")

# class Cat:
#     def __init__(self):
#         print("Cat class constructor")
    
#     def sound(self):
#         print("Meow")

# class Tiger(Cat):
#     def __init__(self):
#         print("Tiger class constructor")
    
#     def sound(self):
#         super().sound()
#         print("Roar")

# tiger = Tiger()
# tiger.sound()

# class Parent:
#     def display(self, child):
#         print("Parent name:", child.parent_name)
#         print("Name:", child.name)
#         print("Age:", child.age)

# class Child(Parent):
#     def __init__(self, parent_name,name, age):
#         print("Child class constructor")
#         self.parent_name = "adfasdf"
#         self.name = name
#         self.age = age
#         super().display(self)


    # def display(self):
    #     print("Parent name:", self.parent_name)
    #     print("Name:", self.name)
    #     print("Age:", self.age)

# child = Child("Parent", "Child", 20)
# child.display()

#inheritance is a relationship between two classes
# class Engine:
#     def __init__(self):
#         print("Engine class constructor")
#     def start(self):
#         print("Engine started")

# class Car():
#     def __init__(self,engine):
#         print("Car class constructor")
#         self.engine = engine
        
#     def drive(self):
#         self.engine.start()
#         print("Driving")

# # compostion
# engine = Engine()
# car = Car(engine)
# car.drive()


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display(self):
#         print(self.title)
#         print(self.author)

# class Library(Book):
#     def __init__(self,name, title, author):
#         super().__init__(title, author)
#         self.name = name
#         self.books = []

#     def display(self):
#         # super().display()
#         if self.books:
#             print(self.books[0].title)
#         else:
#             print("No books available")

#     def add_book(self, book):
#         self.books.append(book)


# library = Library("Bishho Shahitto kendro", "Guido van Rossum", "O'Reilly")
# library.display()

# print("**********")

# book1 = Book("Python", "Guido van Rossum")
# library.add_book(book1)
# library.display()

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display(self):
#         print("Book details")
#         print("title",self.title)
#         print("author",self.author)

# class Library:
#     def __init__(self, name,):
#         self.name = name
#         self.books = []

#     def display(self, book):
#         if self.books:
#             print("Library name:", self.name)
#             book.display()
#         else:
#             print("No books available")

#     def add_book(self, book):
#         self.books.append(book)

# lib = Library("Bishho Shahitto Kendro")
# book1 = Book("Python", "Guido van Rossum")
# lib.add_book(book1) 
# book2 = Book("Java", "James Gosling")
# lib.add_book(book2)

# lib.display(book1)


# circle = pi*r^2
# rectangle = width*height
# triangle = 1/2*base*height



class Shape:
    pi = 3.14
    def __init__(self, name,*args):
        self.name = name
        self.values = args
        print(self.values)

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle", radius)

    def area(self):
        return Circle.pi*self.values[0]**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle", width, height)

circle_area = Circle(5)
print(circle_area.area())
rectangle_area = Rectangle(5, 10)
print(rectangle_area.area())


# Model profile:
#     Name
#     roll
#     address

# Model Employee:
#     profile
#     designation
#     salary
# # Feasibility study
# 1. Economically
# 2. Legal
# 3. Operational
# 4. Technical
# 5. Schedule



# # SDLC MODEL
# 1. Waterfall model
# 2.
# 3. Agile model
# 4. V-model
# 5. Spiral model
# 6. 

# Iterative model incremental model

# signup 
# login

# iterative 
# 1st step : signup + login
# client feedback
# 2nd step: signup + login

# incremental
# 1st step: signup
# client feedback
# 2nd step: login

# Requirement Engineering
#1 feasibility study
#2 Requirement analysis
#3 Requirement validation
#4 Requirement management
