#access modifier
# _ protected, __ private, public

class Car:
    def __init__(self):
        pass
        # self.__updateSoftware()
    def drive(self):
        print('driving')
    def _updateSoftware(self):
        print('updating software')

class Truck(Car):
    def __init__(self):
        pass
        # self.__updateSoftware()
    def drive(self):
        print('driving truck')

class onnoCar():
    def __init__(self):
        pass
        # self.__updateSoftware()
    def drive(self):
        print('driving red car')

redcar = Car()

redcar.drive()
redcar._updateSoftware()

# redcar._Car__updateSoftware() # not accesible from object

truck = Truck()
truck.drive()
truck._updateSoftware()

onnocar = onnoCar()
onnocar.drive()
onnocar._updateSoftware()