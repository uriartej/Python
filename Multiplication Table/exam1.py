from tokenize import Number

number = int(input("Enter number and it will give you a mutiplication of that number: "))
print("You entered", number, "the table will be shown below. Thank you.")

for j in range(1, 11):
   print(number, '*', j, '=', number*j)
   
print("Have a good day.")