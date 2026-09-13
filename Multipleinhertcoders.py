# class P1:
#     def __init__(self):
#         self.name="joshni"
#         self.age=23
#         print(f"{self.name} is {self.age} years old")
# class P2:
#     def __init(self):
#         self.name="janu"
#         self.age=11
#         print(f"{self.name} is {self.age} years old")
# class Child(P1,P2):
#     pass
# Child()


# class P1:
#     def __init__(self):
#         self.name="joshni"
#         self.age=23
#         print(f"{self.name} is {self.age} years old")
# class P2:
#     def __init__(self):
#         self.name="janu"
#         self.age=11
#         print(f"{self.name} is {self.age} years old")
# class Child(P1,P2):
#     def __init__(self):
#         P1.__init__(self)
#         P2.__init__(self)
# Child()



class P1:
    def __init__(self):
        self.name="joshni"
        self.age=23
    def display1(self):
         print(f"{self.name} is {self.age} years old")
class P2:
    def __init__(self):
        self.name="janu"
        self.age=11
    def display2(self):
        print(f"{self.name} is {self.age} years old")
class Child(P1,P2):
        pass


obj=Child()
obj.display1()
obj.display2()  # method ni otside acces cheyali antey by using . and inside use cheyali antey super() method



class P1:
    def __init__(self):
        self.name="joshni"
        self.age=23
    def display1(self):
         print(f"{self.name} is {self.age} years old")


class P2:
    def __init__(self):
        self.name="janu"
        self.age=11
    def display2(self):
        print(f"{self.name} is {self.age} years old")


class Child(P2,P1):
    def __init__(self):
            P2.__init__(self)
        
            P2.display2(self)

Child()





class P1:
    color="white"   # class variable
    def __init__(self):
        self.name="joshni"  # instance variables
        self.age=23
    def display1(self):
        print(f"{self.name} is {self.age} years old and she is {P1.color}" )


class P2:
    def __init__(self):
        self.salary=15000

    def display2(self):
        print(f"{self.name} is getting {self.salary} only")


class Child(P1,P2):
    def __init__(self):
        P1.__init__(self)
        P2.__init__(self)
        print("hello world")
        print(f"{self.name} is {self.age} getting {self.salary}")



obj=Child()
obj.display1()
obj.display2()



class parent1:
    age=23
    def __init__(self,name,role):
        self.name=name
        self.role=role
        print(f"{self.name} is {parent1.age} years and she is {self.role}")
    def display1(self):
        print("hello opps!")


class parent2:
    def __init__(self,salary):
        self.salary=salary
        print(f"{self.name} got {self.salary}")
    def display2(self):
        print("exhausted...")

class child(parent1,parent2):
    def __init__(self,pname,prole,psal):
        parent1.__init__(self,pname,prole)
        parent2.__init__(self,psal)


a=child("joshni","associateeng","15k")
a.display1()
a.display2()
