

for i in range(1,11):
  print(f"5*{i}={5*i}")

for i in range(1,4):
  for j in range(1,11):
    print(f"{i}*{j} = {i*j}")
  print()


for i in range(1,11):
  for j in range(1,11):
    print(f"{i}*{j} = {(i*j)+(i*j)}")
  print() 


# 2*2 
for i in range(1,3):
  for j in range(1,3):
    print("*",end='')
  print()


for i in range(1,3):
  for j in range(1,11):
    print('*',end='')
  print()

for i in range(1,5):
  for j in range(1,5):
    print('*',end='')
  print()

for i in range(1,11):
  for j in range(1,3):
    print('*',end='')
  print()



for i in range(1,3):
  for j in range(1,3):
    print(i,end='')
  print()



for i in range(1,3):
  for j in range(1,3):
    print(j,end='')
  print()


for i in range(1,3):
  for j in range(1,11):
    print(i,end='')
  print()



for i in range(1,11):
  for j in range(1,11):
    print(i,end='')
  print()

# *
# **
# ***
# ****
# *****


for i in range(1,6):
  for j in range(i):
    print("*",end='')
  print()


# *****
# ****
# ***
# **
# *

for i in range(5,0,-1):  
  for j in range(i):
    print("*",end='')
  print()

1
22
333
4444
55555
for i in range(1,6):
  for j in range(i):
    print(i,end='')
  print()
# (or)

for i in range(1,6):
  print(i*str(i))



55555
4444
333
22
1

for i in range(5,0,-1):
  print(i*str(i))



1
23
456
78910
1112131415



n=1
for i in range(1,6):
  for j in range(1,i+1):
    print(n,end='')
    n+=1
  print()




#     1
#    21
#   321
#  4321
# 54321

rows=5
for i in range(1,rows+1):
  print(" " * (rows-i),end='')
  for j in range(i,0,-1):
    print(j,end='')
  print()


#     1
#    12
#   123
#  1234
# 12345

rows=5
for i in range(1,rows+1):
  print(" " * (rows-i),end='')
  for j in range(1,i+1):
    print(j,end='')
  print()


#     1
#    22
#   333
#  4444
# 55555

rows=5
for i in range(1,rows+1):
  print(" " * (rows-i),end='')
  for j in range(1,i+1):
    print(i,end='')
  print()

rows=5
for i in range(1,rows+1):
  print(" " * (rows-i),end='')
  for j in range(i,0,-1):
    print(i,end='')
  print()



# ****1
# ***23
# **456
# *78910
# 1112131415

n=1
rows=5
for i in range(1,rows+1):
  print("*"*(rows-i),end='')
  for j in range(1,i+1):
    print(n,end='')
    n+=1
  print()


# ****1
# &&&21
# ^^321
# %4321
# 54321

rows=5
for i in range(1,rows+1):
  if i==1:
    print("*"*(rows-i),end='')
  elif i==2:
    print("&"*(rows-i),end='')

  elif i==3:
    print("^"*(rows-i),end='')
  elif i==4:
      print("%"*(rows-i),end='')
  for j in range(i,0,-1):
    print(j,end='')
  print()


12345
1234
123
12
1

rows=5
for i in range(rows,0,-1):
  for j in range(1,i+1):
    print(j,end='')
    
  print()

55555
4444
333
22
1

for i in range(5,0,-1):
  for j in range(1,i+1):
    print(i,end='')
  print()


11111
2222
333
44
5
rows=5
for i in range(1,rows+1): 
  for j in range(rows-i+1):
    print(i,end='')
  print()


rows=5
for i in range(1,rows+1): 
  for j in range(i,rows+1):
    print(i,end='')
  print()




11111
1111
111
11
1
rows=5
for i in range(1,rows+1): 
  for j in range(rows-i+1):
    print("1",end='')
  print()





12345
6789
101112
1314
15


n=1
rows=5
for i in range(1,rows+1):
  for j in range(i,rows+1):
    print(n,end='')
    n+=1
  print()




1514131211
10987
654
32
1


n=15
for i in range(5,0,-1):
  for j in range(1,i+1):
    print(n,end='')
    n-=1
  print()




# aaaaa
# aaaaa
# aaaaa
# aaaaa
# aaaaa
rows=5
for i in range(1,rows+1):
  for j in range(1,rows+1):
    print("a",end='')
  print()


rows=5
for i in range(1,rows+1):
  for j in range(1,rows+1):
    print(chr(97),end='')   #ascii values of "a" is 97   and z is 122
  print()

# AAAAA
# AAAAA
# AAAAA
# AAAAA
# AAAAA

rows=5
for i in range(1,rows+1):
  for j in range(1,rows+1):
    print("a",end='')
  print()



# KKKKK
# aaaaa
# KKKKK
# aaaaa
# KKKKK

rows=5
for i in range(1,rows+1):
  for j in range(1,rows+1):
    if i%2!=0:
      print(chr(75),end='')
    elif i%2==0:
      print(chr(97),end='')
  print()

rows=5
for i in range(1,rows+1):
  for j in range(1,rows+1):
    
    if i%2==0:
      print(chr(97),end='')
    else:
      print(chr(75),end='')
  print()



# A
# BC
# DEF
# GHIJ
# KNMNO
rows=5
n=65
for i in range(1,rows+1):
  for j in range(1,i+1):
    print(chr(n),end='')
    n+=1
  print()



# ABCDE
# FGHI
# JKL
# MN
# O


rows=5
n=65
for i in range(rows,0,-1):
  for j in range(i):
    print(chr(n),end='')
    n+=1
  print()



# o
# nm
# lkj
# ihgf
# edcba

rows=5
n=111
for i in range(1,rows+1):
  for j in range(i):
    print(chr(n),end='')
    n-=1
  print()



# ABCDE
# ABCD
# ABC
# AB
# A


rows=5
for i in range(rows,0,-1):
  for j in range(i):
    print(chr(65+j),end='')
  print()




#     *
#    ***
#   *****
#  *******
# *********

rows=5
for i in range(1,rows+1):
  print(" "*(rows-i)+"*"*(i*2-1))


# *********
#  *******
#   ***
#    *


rows=5
for i in range(rows,0,-1):
  print(" "*(rows-i)+"*"*(i*2-1))





#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *


rows=5
for i in range(1,rows+1):
  print(" "*(rows-i)+"*"*(i*2-1))

for i in range(rows,0,-1):
  print(" "*(rows-i)+"*"*(i*2-1))











#     1
#    123
#   12345
#  1234567
# 123456789

rows=5
for i in range(1,rows+1):
  for j in range(rows-i):
    print(" ",end='')
  for j in range(1,i*2):
    print(j,end='')
  print()


#     a
#    abc
#   abcde 
#  abcdefg
# abcdefghi

rows=5
for i in range(1,rows+1):
  char=97
  print(" "*(rows-i),end='')
  for j in range(i*2-1):
    print(chr(char),end='')
    char+=1
  print()



#     a
#    bcd
#   efghi
#  jklmnop
# qrstuvwxy

rows=5
char=97
for i in range(1,rows+1):
  
  print(" "*(rows-i),end='')
  for j in range(i*2-1):
    print(chr(char),end='')
    char+=1
  print()

#     1
#    123
#   12345
#  1234567
# 1234567


rows=5
for i in range(1,rows+1):
  print(" "*(rows-i),end='')
  for j in range(i*2-1):
    print(j+1,end='')
  print()



# 123456789
#  1234567
#   12345
#    123
#     1

rows=5
for i in range(rows,0,-1):
  print(" "*(rows-i),end='')
  for j in range(i*2-1):
    print(j+1,end='')
  print()



#  123
#   12345
#  1234567
# 123456789
# 123456789
#  1234567
#   12345
#    123
#     1


rows=5
for i in range(1,rows+1):
  print(" "*(rows-i),end='')
  for j in range(i*2-1):
    print(j+1,end='')
  print()
for i in range(rows,0,-1):
  print(" "*(rows-i),end='')
  for j in range(i*2-1):
    print(j+1,end='')
  print()


#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI
# ABCDEFGHI
#  ABCDEFG
#   ABCDE
#    ABC
#     A


rows=5
for i in range(1,rows+1):
  char=65
  print(" "*(rows-i),end='')
  for j in range(2*i-1):
    print(chr(char),end="")
    char+=1
  print()

rows=5
for i in range(rows,0,-1):
  char=65
  print(" "*(rows-i),end='')
  for j in range(2*i-1):
    print(chr(char),end="")
    char+=1
  print()



#     !
#    !"#
#   !"#$%
#  !"#$%&'
# !"#$%&'()


rows=5
for i in range(1,rows+1):
  char=33
  print(" "*(rows-i),end='')
  for j in range(2*i-1):
    print(chr(char),end="")
    char+=1
  print()


# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *

rows=5
for i in range(1,rows+1):
  for j in range(1,i+1):
    print("*",end='')
  print()
  

for i in range(rows,0,-1):
  for j in range(1,i+1):
    print("*",end='')
  print()



# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
k=4
for i in range(1,11):
  if i<=5:
    print("*"*i)
  else:
    print("*"*k)
    k-=1






1
01
101
0101
10101


rows=5
for i in range(1,rows+1):
  for j in range(1,i+1):
    if (i+j)%2==0:
      print(1,end='')
    else:
      print(0,end='')
  print()

# 1      1
# 12    21
# 123  321
# 12344321

rows=4
for i in range(1,rows+1):
  logic=(rows*2)-(i*2)
  
  for j in range(1,i+1):
    print(j,end='')

  print(" "*logic,end='')
  for j in range(1,i+1):
    print(j,end='')
  print()
