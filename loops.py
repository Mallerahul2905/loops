# Print all numbers from 1 to 100 using a for loop.
# for i in range(1,101):
#     print(i)

# Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)

# n=int(input('Enter a number:'))
# if n<0:
#     print('Enter valid number:')
# else:
#     sum = (n*n+1/ 2)  
#     print(sum) 

# Print all even numbers between 1 and 50 using a while loop.

# num = 1
# while num<=50:
#     if num%2==0:
#         print(num)
#     num+=1

# Write a program to display the multiplication table of a given number. First 20
# num1 = int(input('Enter a number:'))
# for i in range(1,21):
#     for j in range(1,11):
#         print(i,'*',j,'=',i*j)

# Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits

# num1 = 54321
# reverse=0
# count=0
# sum=0
# while num1 >0:
#     rem = num1 %10 #1 #2 #3 #4 #5 
#     reverse=reverse*10+rem
#     print(rem)
#     sum+=rem
#     count+=1
#     num1 = num1 // 10 #5432 #543 #54 #5 #0   #(5432.1 so we get 5432)
# print(reverse)
# print(sum)
# print(count)


# enter numbers until they enter neagative number
# while True:
#     num=int(input("enter a number:"))
#     if num<0:
#        print("Negative")
#        break

# Medium


# fabonacci series
# num1 = 0
# num2 = 1
# # sum=0
# for i in range(1,11):
#     print(num1)
#     num1,num2=num2,num1+num2

# given number is prime or not

# n=12
# temp=True
# for i in (2,n+1):
#     if n%i==0:
#         print("not a prime")
#         break
#     else:

#          print("prime")

# Implement a menu-driven program where the user can
# choose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit.

# for i in range(1,101):
#    if i % 15 == 0:
#     print(i)

# print("1.square")
# print("2.cube")
# print("3.exit")
# choose=int(input("Enter a number:"))
# if choose==1:
#     num=int(input("Enter a number:"))
#     print(num**2)
# elif choose==2:
#      num=int(input("Enter a number:"))
#      print(num**3)
# elif choose==3:
#      print("Exit")
# else:
#      print("NUN")