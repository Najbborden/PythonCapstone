import time
import os
user = os.getlogin()
print("Programmer:", user)
print(time.strftime('Lab 19.2 %m/%d/%Y @ %H:%M:%S\n'))
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def setName(self, name):
        self.__name = name

    def setNumber(self, number):
        self.__number = number

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number


class Worker(Employee):
    def __init__(self, name, number, shift, hourly):
        super().__init__(name, number)
        self.__shift = shift
        self.__hourly = hourly

    def str(self):
        return \
            "Name: " + self.getName() + "\n" + \
            "ID number: " + self.getNumber() + "\n" + \
            "Shift: " + self.getShift() + "\n" + \
            "Hourly Pay Rate: $" + self.getHour()

    def setShift(self, shift):
        self.__shift = shift

    def setHour(self, hourly):
        self.__hourly = hourly

    def getShift(self):
        return self.__shift

    def getHour(self):
        return self.__hourly


def main():
    name = input("Enter your name: ")
    empl1 = Worker("", 0, 0, 0)
    employee_name = input("Enter the employee's name: ")
    empl1.setName(employee_name)
    id_number = int(input("Enter the ID number: "))
    empl1.setNumber(id_number)
    shift = int(input("Enter the shift number: "))
    empl1.setShift(shift)
    hour = int(input("Enter the hourly pay rate: "))
    empl1.setHour(f"{hour:,.2f}")
    print(f"{name}, here is the production worker, {empl1.getName()}'s information:\n")
    print(empl1)
main()