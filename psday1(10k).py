# print digits of anumber with type casting
n=1234
a=str(n)
for i in a:
    print(i)



# print digits of anumber without type casting

n=1234
while n>0:
    digit=n%10
    print(digit)
    n=n//10





# print digits of anumber without type casting and print evensum and oddsum.
n=1234
evensum=0
oddsum=0
while n>0:
    digit=n%10
    print(digit)
    if digit%2==0:
        evensum+=digit
    else:
        oddsum+=digit


    n=n//10
print(evensum)
print(oddsum)




# print sum of digits in a number
n=1234
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)




n=12345
count=0
while n>0:
    # digit=n%10
    count+=1
    n=n//10
print(count,"total no.of digits")



# prime number or not
n=7      # negative nums,0,1 are not prime numbers
count=0
for i in range(1,n+1):
  if n%i==0:
    count+=1
if count==2:
  print("prime")
else:
  print("not prime")



  