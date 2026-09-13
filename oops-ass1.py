# Create a class Greeter with a method greet(name) that prints a greeting for the provided name

class Greeter:
    def greet(self,name):
        print("hello",name)
obj=Greeter()
obj.greet("joshni")


# Develop a class Calculator with methods to add and subtract two numbers

class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        print(self.x+self.y)
    def subtract(self):
        print(self.x-self.y)
o=Calculator(45,23)
o.add()
o.subtract()





# Build a class Employee with multiple constructors that can initialize an employee object in different ways.
# output should be like
# Name: John
# Name: Doe
# ID: 101
# Name: Jane
# ID: 102
# Department: HR



class Employee:
    def __init__(self,name,id=None,department=None):
        self.name=name
        self.id=id
        self.department=department
    def display(self):
        print("Name:",self.name)
        if self.id is not None:
            print("ID:",self.id)
        if self.department is not None:
            print("ID:",self.department)
a=Employee("John")
b=Employee("Doe","101")
c=Employee("jane","102","HR")

a.display()
print()
b.display()
print()
c.display()

# Create a class MaxFinder that identifies the largest number in a list.
# output:
# The largest number is: 5

class MaxFinder:
    def __init__(self,nums):
        self.nums=nums
    def display(self):

        largest=max(self.nums)
        print(f"The largest number is {largest}")

obj=MaxFinder([1,2,3,6,4])
obj.display()