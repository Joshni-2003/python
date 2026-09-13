# multiple inheritance:one child class inherits properties and methods from morethan one parent class

class p1:
    def __init__(self):
        self.name="x"
    def display1(self):
        print(f"{self.name} is in parentp1 class")


class p2:
    def __init__(self):
        self.name="y"
    def display2(self):
        print(f"{self.name} is parentp2 class")


class child(p1,p2):
    def __init__(self):
        self.name="z"
        # p1.display1(self)
        # p2.display2(self)
        p1.__init__(self)    # here p1 lo init method chesam kabati x print ayidhi alane p2 init method chesam kabati y print ayidhi
        p1.display1(self)
        p2.__init__(self)
        p2.display2(self)

child()


#same pgms there is a small change in the code below

class p1:
    def __init__(self):
        self.name="x"
    def display1(self):
        print(f"{self.name} is in parentp1 class")


class p2:
    def __init__(self):
        self.name="y"
    def display2(self):
        print(f"{self.name} is parentp2 class")


class child(p1,p2):
    def __init__(self):
        self.name="z"                #class p1 lo __init__() method call cheyaledhu kabati x ki velladhu ,p2 kuda cheyaledhu kabati y ki velladhu only z matarm print ayidhi
        p1.display1(self)
        p2.display2(self)
        

child()






class p1:
    def __init__(self):
        self.name="x"
    def display1(self):
        print(f"{self.name} is in parentp1 class")


class p2:
    def __init__(self):
        self.name="y"
    def display2(self):
        print(f"{self.name} is parentp2 class")


class child(p1,p2):
    def __init__(self):
        self.name="z"
        p1.__init__(self)   # p1 ni  __init__ tho call chesam kabatai both x print avutayi manam p2 lo __init__call cheyaledhu kabti y ki poddhu
        p1.display1(self)
        p2.display2(self)
        

child()


class p1:
    age=23
    def __init__(self,f_name):
        self.fathername=f_name
        print(f"{self.fathername} is p1 class")


class p2:
    age=25
    def __init__(self,m_name):
        self.mothername=m_name
        print(f"{self.mothername} is p2 class")


class child(p1,p2):
    def __init__(self,fname,mname,myname):
        p1.__init__(self,fname)
        p2.__init__(self,mname)
        print(p1.age)
        print(p2.age)


child("ram","rani","raju")






# multi-level inheritance-



class grandparent:
    def __init__(self,g_name):
        self.d=g_name
        print(f"{self.d} is grandparent class")

class parent(grandparent):
    def __init__(self,p_name,g_name):
        super().__init__(g_name)
        self.c=g_name
        print(f"{self.c} is parent class")

class child(parent):
    def __init__(self,c_name,p_name,g_name):
        super().__init__(p_name,g_name)
        self.b=c_name
        print(f"{self.b} is child class")


class grandchild(child):
    def __init__(self,gc_name,c_name,p_name,g_name):
        super().__init__(c_name,p_name,g_name)
        self.a=gc_name
        print(f"{self.a} is in grandchild class")

grandchild("susila","prasad","dharani","nayani")









class grandparent:
    def __init__(self,g_name):
        self.name1=g_name
        print(f"{self.name1} is grandparent class")

class parent(grandparent):
    def __init__(self,p_name,g_name):
        super().__init__(g_name)
        self.name2=p_name
        print(f"{self.name2} is parent class")

    
class child(parent):
    def __init__(self,c_name,p_name,g_name):
        super().__init__(p_name,g_name)
        self.name3=c_name
        print(f"{self.name3} is child class")
child("venkat","venu","satya")










#hierarchial inheritance:more than one child class inherits properties and methods from single parent class


class parent:
    age=23
    def __init__(self,e_name,e_role):
        self.na=e_name
        self.rol=e_role
        self.a="ramu"
        print(f"{self.a} is a good boy")
    def display1(self):
        print(f"This is joshni and her age is {parent.age}")

class child1(parent):
    age=25
    def __init__(self,name,role):
        self.name=name
        self.role=role
        super().__init__(name,role)
        print(f"{self.name} is a {self.role}")
           
class child2(parent):
    def __init__(self,name,role):
        
        print("welcome back to python world")
        super().__init__(name,role)
        super().display1()
      
child2("fghj","ghj")
child1("joshni","ass.eng")



# ex:2

class parent:
    age=25
    color="white"
    def __init__(self,name,role):
        self.name=name
        self.role=role
        
class child1(parent):
    
    def __init__(self,pname,prole):
        
        super().__init__(pname,prole)
        print(f"There are so many colors but i like only {child1.color}")
        
class child2(parent):
    def __init__(self,ename,erole):
        print("fullstack developer")
        super().__init__(ename,erole)
        print(f"{self.name} is {parent.age} and she is {self.role}")
               
child2("joshni","developer")
child1("venu","tester")