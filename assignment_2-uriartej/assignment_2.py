import re
from calculation import *

name = input("Enter your name ")
print("My name is " + name)

phonenumber = int(input("Enter phonenumber "))
print("My Phone Number is " , phonenumber)

username = input("Enter Username: ")
print("Username is: " + username)

num = int(input("Enter Number "))
print(number(num))

grade = int(input("Enter your Score: "))
print(score(grade))

evenodd = [1,2,3,4,5,6,7,8,9,0]

evencount = 0
oddcount = 0

for val in evenodd:
    if (val % 2 == 0):
        evencount += 1
    else:
        oddcount += 1
        
print("evencount" ,evencount )
print("oddcount" ,oddcount)

print(range(13))

print(list(range(15)))

print(list(range(23, 30)))

print(list(range(5,25,4)))

lang = ("PYTHON", "JAVA", "C", "C++")

for val in range(len(lang)):
    print(lang[val].upper())

count = 0
while count < 10:
    count += 3
    print("Python Loops")

numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]

for i in range(len(numbers)):
    numbers[i]=numbers[i]**2
print(numbers) 
print(sum(numbers))

student_name_1 = 'Mayur'
student_name_2 = 'Sam'

print(rollcall(student_name_1))
print(rollcall(student_name_2))

target = 7



print(result)
# print(list(result))


# area of trianle
area_of_triangle (3, 4, 5)

#area of circle
area_of_circle (3)

#area of square
area_of_square (5)

#area of rectangle
area_of_rectangle (3, 5)