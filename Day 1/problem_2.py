
# find the perfect square

import math

num = int(input("Enter a number to check if it is a Perfect square"))
root = int((math.sqrt(num)))
root = math.floor(math.sqrt(num))
result= root * root

if( result == num):
    print("Input Number is PS")
else:
    print("Input Number is Not PS")

          