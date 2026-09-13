# oop:object oriented pgmng 

# class:blueprint or design to create objects (or) contains attributes(variables) and methods(functions)

# class House:
#     a=10
#     b="joshni"
#     print(a)
#     print(b)
#     def display(self):
#         print("welcome to python")
#     display("janu")


class Parent:
    def __init__(self,name,age,color):
        self.abc=name
        self.xyz=age
        self.mno=color
        print(f"{self.name} is mental")
    def myprop(self):
        pass
class Child(Parent):
    def __init__(self,name,age,color):
        super().__init__()
        pass
a=Child("joshni",23,"black")



class Parent:
    def __init__(self,name,age,color):
        self.abc=name
        self.xyz=age
        self.mno=color
        print(f"{self.abc} is mental")
    def myprop(self):
        print("hello welcome to python world")
class Child(Parent):
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
        super().__init__(name,age,color)
        print("hello,good evening")
        super().myprop()
        pass
a=Child("joshni",23,"black")



