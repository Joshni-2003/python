# oops:object oriented programming , oop is a pgmng paradigm that organizes code using classes and objects
# there r 4 pillars:1.encapsulation , 2.inheritance , 3.polymorphism, 4.abstraction
# class,object:main syntax for oops
# reusable(code reuse),scalable(efficient) and modular(separate)
# why we need opps
# 1.we can bulid scalable large applications
# 2.we can reuse the code 
# 3.we can make the code modular
# class:blueprint for creating objects
# object:instance of class


# class House:
#     print("welcome to python")


# class House:
#     print("python is easy")
# House()
# print("hello world")

# class House:
#     def __init__(self,floors,color,cost):  # instance method,constructor method and default constructor
#         print(self)
#         print(floors)
#         print(color)
#         print(cost)
#     __init__(10,4,'black','20 lakh')



# class House:
#     def __init__(self,floors,color,cost):  # instance method,constructor method and default constructor  ,self-keyword
#         print(self)
#         print(floors)
#         print(color)
#         print(cost)
    
# House(2,'white','20')



# class House:
#     def __init__(self,floors,color,cost):  #  self-object or current instance of class
#         self.a=floors
#         self.b=color
#         self.c=cost
#         print(self.a)
# House(2,'orange',20)
# House(3,'pink',25)



# can we take 2 default constructors :yes it's overrides the first one
# class Home:
#     def __init__(self,floors,color,cost):

#         self.a=floors
#         self.b=color
#         self.c=cost
#         print(self.a)
#         print(self.b)
#         print(self.c)

#     def __init__(self,floors,color,cost):
        
#         self.a=floors
#         self.b=color
#         self.c=cost
#         print(self.a)
#         print(self.b)
#         print(self.c)

# Home(2,'pink',20)
# Home(4,'orange',50)


class Home:
    def __init__(self,floors,color,cost):  # classs is having some code which will be exucuted aautomatically
        
        print(self)
        print(floors)
        print(color)
        print(cost)
    __init__(10,5,'green',55)
        
Home(2,'white',20)








































