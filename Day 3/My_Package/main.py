import nums

num1 = 15
num2 = 25
num3 = 37
num4 = 20
num5 = 55

from nums import check_if_even
from nums import check_if_odd
from nums import check_if_prime

if check_if_even(num1):
    print(f'{num1} is Even')

else:
    print(f'{num1} is not even')


if check_if_odd(num1):
    print(f'{num1} is Odd')

else:
    print(f'{num1} is not Odd')

if check_if_prime(num1):
    print(f'{num1} is Prime')

else:
    print(f'{num1} is not Prime')