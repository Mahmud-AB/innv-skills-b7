# What does the __init__ method in a class do?
# class Student:
#     def __init__(self):
#         print("init")

# obj = Student()

# What will be the output of this code?
# class Account:
#     interest_rate = 0.05

#     def __init__(self, balance):
#         self.balance = balance
    
#     def apply_interest(self):
#         self.balance += self.balance * Account.interest_rate
    
#     def set_interest(self, rate):
#         self.interest_rate = rate

# savings = Account(1000)
# savings.set_interest(0.01)
# savings.apply_interest()
# print(savings.balance)

# What is the return value of the following code?

# class Test:
#     def __init__(self):
#         self.x = 10
    
# obj = Test()
# print(obj.x)

# What is the return value of the following code?
# class Delta:
#     def __init__(self):
#         print("delta")
#         self.__sigma = "hidden"

# class Gamma(Delta):
#     def __init__(self):
#         print("init")
#         super().__init__()
#     def reveal(self):
#         return self.__sigma
    
# obj = Gamma()
# print(obj.reveal())

# What is the return value of the following code?
# class Enigma:
#     def __init__(self):
#         self.__hidden = "secret"

# obj = Enigma()
# obj.__hidden = "exposed"
# print(obj._Enigma__hidden)
# print(obj.__hidden)

import json
import os

def load_file():
    if os.path.exists("case.json"):
        with open("case.json","r") as file:
            return json.load(file)

def view_all_cases(cases):
    if not cases:
        print("not cases found")
    else:
        for case_id,case_details in cases.items():
            print(f"Case ID : {case_id}")
            print(f"Title: {case_details['Title']}")
            print(f"Suspect:{', '.join(case_details['Suspect']) if case_details['Suspect'] else 'None'}")
            print(f"Status: {case_details['Status']}")
            
    
def main():
    cases = load_file()
    while True:
        choice = input()
        if choice == "1":
            view_all_cases(cases)
            
if __name__ == "__main__":
    main()