
# Math table

input_number = int(input("Enter the number to print the math table : \n"))
i = 1
while (i<=10) :
    product = input_number * i
    print ('%d * %02d = %03d' % (input_number,i,product))
    i = i + 1

