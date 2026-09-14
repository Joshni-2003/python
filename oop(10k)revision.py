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




# multi-level inheritance


class order:
    def __init__(self,oid,op):
        # print(oid,op)
        self.id=oid
        self.opay=op
        # print(self.id)
        # print(self.opay)
        print(self.id,self.opay)
    def show2(self):
        print(f"payment method is {self.opay}")
        
class onlineorder(order):
    def __init__(self,orderid,orderpayment,orderitems):

        # print(orderid,orderpayment,orderitems)
        self.orderid=orderid
        self.op=orderpayment
        self.i=orderitems
        # print(self.orderid)
        # print(self.op)
        # print(self.i)
        print(self.orderid,self.op,self.i)
        super().__init__(orderid,orderpayment)
    def show1(self):
        print(f"{self.orderid} with order items are {self.items}")
        super().show2()
class fastorder(onlineorder):
    def __init__(self,id,name,items,payment):
        # print(id,name,items,payment)
        self.id=id
        self.name=name
        self.items=items
        self.payment=payment
        print(self.id,self.name,self.items,self.payment)
    
        super().__init__(id,payment,items)
    # def show(self):
    #         print("order successfull")
        super().show1()

obj=fastorder(101,"joshni",["mango","apple","banana"],"upi")
# obj.show()


# multiple inheritance:---more than one parentt

class mapsystem:
    def __init__(self,na,add,dr):
        self.na=na
        self.add=add
        self.dres=dr
    def mapdetails(self):
        pass
class paymentsystem:
    def __init__(self,nam,addr,payment):
        self.nam=nam
        self.addr=addr
        self.payment=payment
    def paymentdetails(self):
        pass
class deliveryperson(mapsystem,paymentsystem):
    def __init__(self,n,d,a,p):
        self.name=n
        self.dress=d
        self.address=a
        self.payment=p
        print(self.name,self.dress,self.address,self.payment)
        mapsystem.__init__(self,n,a,d)
        paymentsystem.__init__(self,n,a,p)
    def orderdelivered(self):
        print(f"{self.name} ordered {self.dress} dress with {self.payment} method")


obj=deliveryperson("joshni","anarkali","tiruvuru","upi")
obj.orderdelivered()





# Another example:

class mapsystem:
  def __init__(self,n,l):
    # print(n)
    # print(l)
    # self.name=n
    # self.loc=l
    # print(self.name)
    # print(self.loc)
    print(f"{self.n} ordered to the location {self.l}")
  def show1(self):
    print(f"The order comes to {self.l} address")
class paymentsystem:
  def __init__(self,n,p):
    # print(n)
    # print(p)
    print(f"{self.n} proceed the payment through {self.p} method")
  def show2(self):
    print(f"The method is {self.p}")
class deliveryperson(mapsystem,paymentsystem):
  def __init__(self,name,location,payment,dress):
    # print(name)
    self.n=name
    self.l=location
    self.p=payment
    self.a=dress
    print(self.n,self.l,self.p,self.a)
    mapsystem.__init__(self,name,location)
    paymentsystem.__init__(self,name,payment)
    # super().show1()
  
    # mapsystem.show1(self)
    # paymentsystem.show2(self)
    super().show1()
    super().show2()
  def show3(self):
    print(f"{self.n} receives the order successfully")
    
    
obj=deliveryperson("joshni","tvr","upi","lehanga")
obj.show3()





















