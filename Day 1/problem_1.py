
# find the greatest number


num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))

if ((num1 > num2 ) and (num1 > num3)):
    print("is the biggest number" + str(num1))
elif (num2 > num3):
    print("is the biggest number" + str(num2))
else:
    print("is the biggest number" + str(num3))