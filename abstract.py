from abc import ABC, abstractmethod

# class Vehicle(ABC):  # Abstract Base Class
#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):
    
#     def start(self):
#         print("Car is starting")

#     def stop(self):
#         print("Car is stopping")

# car = Car()
# car.start()
# car.stop()


class Payment(ABC):
    @abstractmethod
    def payment(self):
        pass
    
class CashPayment(Payment):
    def payment(self):
        print("Cash payment")

class CreditCardPayment(Payment):
    def payment(self):
        print("Credit card payment")
