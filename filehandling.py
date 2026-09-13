# a=open("file.py","r")
# print(a.read())


# with open("file.py","r") as a:
#     print(a.read())


# with open("file.py","r") as a:
#     print(a.readline())
#     print(a.readline())

#     a.close()



# with open("file.py","r") as a:
#     print(a.read(6))


with open("file.py","a") as a:
    a.write("file handling")

with open("file.py","r") as a:
    print(a.read())
