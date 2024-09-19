
# 2nd smallest digit digit in a number 



num = int(input("Enter the number"))

small = 9
sec_small = 9
temp = num


while temp !=0:
    rem = temp % 10
    temp = temp //10

    if rem < small:
        small = rem
        sec_small = rem
    elif rem < sec_small:
        sec_small = rem

print(sec_small)