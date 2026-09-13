a=10
print(type(a))   #<class 'str'>   ---angular brackets(<>) lo class vachi vuntey dani object antaruuu
b="joshni"           #  1 st <> undali 2nd class aney keyword undali
print(type(b))    # in python everything is an object  
def func():
    pass
func()
print(type(func)) # 1.memory lo store ayedhi variables and functions,   2.type check cheyali


# oops:
# 1.class : it is a blueprint for creating objects.
# 2.object: instance of a class.
# 3.attributes:variables
# 4.methods:functions
# 5.self:current object
# 6.__init__: default constructor


class amazon:
    def __init__(self):
        pass
    def Show(self):
        pass
obj=amazon()
print(obj)
obj.Show()


class amazon:
    def __init__(self,b,p,c):
        print(b)
        print(p)
        print(c)
        print("hello")
    def Show(self,b):
        print(b)
obj=amazon("iqoo",25000,"black")
print(obj)
obj.Show("vivo")



class amazonproduct:
    def __init__(self):
        self.brand="iqoo"   # variables antey self.brand
        self.price=25000
        self.color="black"
        print(self.brand)  # store chsekunna variables use cheyachu method lo
        print(self.price)
        print(self.color)  
    def Show(self):
        print(self.brand)
        print(self.color)
        print(self.price)
obj=amazonproduct()
obj.Show()




class amazonproduct:
    def __init__(self,b,p,c):
        self.brand=b   # variables antey self.brand
        self.price=p
        self.color=c
        print(self.brand)  # store chsekunna variables use cheyachu method lo
        print(self.price)
        print(self.color)  
    def Show(self):
        print(self.brand)
        print(self.color)
        print(self.price)
obj=amazonproduct("iqoo",25000,"white")
obj.Show()






class amazonproduct:
    platform="amazonplatform"  # cls variable
    print(platform)
    def __init__(self,b,p,c):
        self.brand=b   # variables antey self.brand
        self.price=p
        self.color=c      # instance variable antey color,price,brand
        # print(platform)   (wrong)
        print(self.platform)    # clas variable ayina instance variable ayina "self" kachitam ga vadali
    def Show(self):
        print(self.brand)
        print(self.color)      
        print(self.price)
        
obj=amazonproduct("iqoo",25000,"white")
obj.Show()
obj1=amazonproduct("laptop",13000,"black")
obj1.Show()





class Product:
    def __init__(self,b,c,p):
        self.brand=b
        self.color=c
        self.price=p

        
    def Show(self):
        print(self.brand)
        print(self.color)
        print(self.price)
    def disc(self,discu):
        discount=(self.price*discu)/100
        print(discount)
        total_purchase=(self.price-discount)
        print(total_purchase,"total_amount")
obj=Product("iqoo","black",27000)
obj.Show()
obj.disc(5)




# oops ----day2(Inheritance)



class Parent:
  platform="hyd"
  # print(platform)
  def __init__(self,pname,prole,page):
    self.abc=pname
    self.mno=prole
    self.xyz=page
    print(self.abc)
    print(self.mno)
    print(self.xyz)
    # print(Parent.platform)
  def show(self):
    print("welcome to oops")
      
    
    
    
class Child(Parent):
  def __init__(self,n,r,a):
    self.name=n
    self.role=r
    self.age=a
    print(self.name)
    print(self.role)
    print(self.age)
  
    super().__init__(n,r,a)
  def Shows(self):
    print("hello python")
    # print(Parent.platform)
    super().show()
    
obj=Child("joshni","associate eng",23)
print(Parent.platform)
obj.Shows()
























