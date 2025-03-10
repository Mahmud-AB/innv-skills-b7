class SmartDevice:
    def __init__(self,name):
        self.name = name

class Light(SmartDevice):
    def __init__(self,name):
        super().__init__(name)
        self.state = "off"

    def toggle(self):
        self.state = "on" if self.state == "off" else "off"
        print(f"{self.name} is now {self.state}")

class Thermostat(SmartDevice):
    def __init__(self,name):
        super().__init__(name)
        self.temperature = 72
    def set_temperature(self,temperature):
        self.temperature = temperature
        print(f"{self.name} temperature is now {self.temperature}")

class SmartHome:
    def __init__(self):
        self.devices = {}
    
    def add_device(self,device):
        self.devices[device.name] = device
    def list_devices(self):
        print("devices:", ",".join(self.devices.keys()))
    
    def control_device(self,name,command,value=None):
        if name in self.devices:
            print(self.devices[name])
            device = self.devices[name]
            if command == "toggle":
                device.toggle()
            elif command == "set_temp":
                device.set_temperature(value)
            else:
                print("Invalid command")

home = SmartHome()

while True:
    try:
        command = input("Enter command:")
        if command == "add":
            command =  input("Enter device type:1.light 2.thermostat")
            name = input("Enter device name:")
            if command == "1":
                home.add_device(Light(name))
            elif command == "2":
                home.add_device(Thermostat(name))
            else:
                print("Invalid device type")
        elif command == "list":
            home.list_devices()
        elif command == "toggle":
            name = input("Enter device name:")
            home.control_device(name,"toggle")
        elif command == "set_temp":
            name = input("Enter device name:")
            value = input("Enter temperature:")
            home.control_device(name,"set_temp",int(value))
        else:
            print("Invalid command")
    except EOFError:
        break