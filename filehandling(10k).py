# create file and write one line.
a=open("joshni.txt","w")
a.write("hello python welcome to file handling\n")


# f=open("janu.txt","x")    # to create we use 'w'
# f.write("hello python file handlind is one of the most important topic in python")

f=open("jyoti.txt","x")
f.write("hello python file handlind is one of the most important topic in python")



# create  python file and write multiple lines.
b=open("add.py","w")
b.write("a=100\nb=100\nc=a+b\nprint(c)")


# when we read the file the file must be there.
f=open("add.py","r")
print(type(f.read()))     
f.close()

f=open("add.py","r")
print(f.read())      # reads entire file
f.close()


f=open("add.py","r")
print(f.readline())   # read one line


f=open("add.py","r")
print(f.readlines())    # list of strings



 # append means add the end of the file.
f=open("add.py","a")   # kepps existing file like that adds at the end of the file
f.write("\nfruits=['apple','banana','orange']")


# delete the file
import os 
if os.path.exists("add.py"):
    os.remove("add.py")
else:
    print("no file found")


# we have to read the file and write 
f=open("joshni.txt","r+")
print(f.read())    # read means genral  we have to console means print  
f.write("\nfile handling is one of the important topic in python")
f.close()



a=open("joshni.txt","r+")
print(a.read())                        # nuvu append pettakapoyina r+ both read and write chesthunav kabati append ayidhi
a.write("\ngood morning have u a nice day...")


with open("pgms.py","r") as s:
    for i in s:
        print(i)




with open("pgms.py","r") as s:
    for i in s:
        print(i.strip())



x=open("add.py","r")
print(x.read())


try:
    a=open("add.py","r")
    print(a.read())
except FileNotFoundError:
    print("try to acess and hadles the file...")
print("filehandling")



a=open("add.py","a")
print(a.read())



# handling errors while doing file handling
import io
try:
    # a=open("add.py","a")
    a=open("add.py","w")
    x=a.write("\na=200")
    print(x)
except FileExistsError:
    print("file already exist create new filewith new name")

    # print(a.read())
except FileNotFoundError:
    print("try to acess and hadles the file...")
except io.UnsupportedOperation:
    print("use proper operation")
print("filehandling")


import os 
# os.mkdir("pandas")  # crteas a folder
# os.rmdir("pandas")   # remove directory


# os.path.exists("janu.py")  # to check file is there or not
# os.remove("janu.py")   # deletes file
os.rename("add.py","addition.py")  # rename file
# note we cannot delete the folder directly but we can delete the file