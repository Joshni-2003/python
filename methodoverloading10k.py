# method overriding and overloading and polymorphism...

# method overriding: diff clses same method name.  
# method overriding:child cls provides nwe implementation from its parentclass
class car:
    def __init__(self):
        pass
    def display(self):
        name="toyata"
        price="20lakhs"
        color="black"
        print(f"The {name} is {price} and {color} color")
class bike:
    def __init__(self):
        pass
    def display(self):
        name="royalenfield"
        price="10lakhs"
        color="red"
        print(f"The {name} is {price} and {color} color")


carobj=car()
carobj.display()
bikeobj=bike()
bikeobj.display()


# method overriding

class netflixuser:
    def __init__(self):
        self.name="generaluser"
        print(f"{self.name} uses netflix")
    def accessdashboard(self):
        print("welcome back too netflix....")
class netflixadmin(netflixuser):
    def __init__(self):
        self.name="admin"
        print(f"{self.name}user")
    def accessdashboard(self):
        print("welcome to adminuser he can add or remove")

admin=netflixadmin()
user=netflixuser()
admin.accessdashboard()
user.accessdashboard()


# method overloading:one class same method name oe or more methods diff params.


class swiggyorder:
    def __init__(self):
        pass
    def paymentorder(self,*a):
        print(a)

obj=swiggyorder()
obj.paymentorder("birayani")
obj.paymentorder("birayani",'roti',"coke")

#2nd example

class swiggyorder:
    def __init__(self):
        pass
    def paymentorder(self,*a):
        if a[0]=="birayani":
            print("biryani order placed")


obj=swiggyorder()
obj.paymentorder("birayani")
obj.paymentorder("birayani",'roti',"coke")


# 3 rd example
class swiggyorder:
    def __init__(self):
        pass
    def paymentorder(self,*a):
        if a[0]=="birayani" and len(a)<=1:

            print("biryani order placed")
        elif a[1]=="roti" and len(a)>=1:
            print("3 items are places successfully")
        else:
            print("no items are placed")

obj=swiggyorder()

obj.paymentorder("birayani")
obj.paymentorder("birayani",'roti',"coke")




