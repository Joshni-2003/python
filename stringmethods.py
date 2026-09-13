a="joshni IS dirty"
print(a.title())

print(a)
print(len(a))
count=0
for i in a:
    count+=1
print(count)

print(type(a))
print(a[0])


# print(a.upper())
b=a.upper()
print(b)

print(a.capitalize())
c=a.capitalize()
print(c)
print(a.swapcase())


x="WelcOme tO pYTHon world"
y=[]
z=[]
countu=0
countv=0
for i in x:
    if i.isupper():

        y.append(i)
        if i in "aeiouAEIOU":
            countu+=1
        
    else:
        z.append(i)
        if i in "aeiouAEIOU":
            countv+=1
            
print(y)
print(z)
print(countu)
print(countv)


x="123"
print(x.isdigit())



y="py12345"
print(x.isalnum())



a="python123 is Easy and Opensource"
b=[]
for i in a:
    if i.isalpha():
        if i.isupper():
            if i in "aeiouAEIOU":
                b.append(i)
print(b)


a="fghjk2345678$$%^&^%$#@"
b=[]
for char in a:
    if not  char.isalnum() and not char.isspace():
        b.append(char)
print(b)


a="welcomepython"
print(a.index("p"))
print(a.rindex("w"))
print(a.find("z"))


username=input("enetr:-----")
userpswd=int(input("enter:----"))
users=[{"name":"joshni","password":12345},{"name":"janu","password":56784}]
for i in users:
    # print(i)
    if username==i["name"] and userpswd==i["password"]:
        print("login succes")
        break
        
else:
    print("invalid credentials")


a=" sfghj        "
print(a.strip())  # to remove spaces from both sides of the str
print(a.rstrip())  #to remove spaces from rightside of the str
print(a.lstrip())  # o remove spaces from leftside of the str


x="ertyui @#ert"
print(x.split("@"))  # split is used to split the str base on a ref char into list of items
print(x.split())

y="developer"
print(y.split("e"))


a=["ram","ravi","joshni"]
a=("janu","josh","jyothi")  
b="-".join(a)    # join method is used to join the list of items into a single str with ref including
print(b)

z="vamsienduri"
print(z.replace("i","%"))

print("venupalagani".replace("a","%"))

a={"name":"joshni","age":23,"role":"engineer"}
a["name"]="janu"
print(a)

a["studentname"]=a["name"]
del a["name"]
print(a)


a="python is easy to learn"
print(a.startswith("python"))
print(a.endswith("easy"))


s="developer"
print(s[0:3])
print(s[::-1]) # backwardstep

print(s[0::8])















