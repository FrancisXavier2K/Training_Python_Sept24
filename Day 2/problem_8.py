# Find the sum of the numbers entrered via the command line
import sys

numbers = sys.argv
sum = 0
for i in range(1, len(numbers)):
    sum += float(numbers[i])
print(f'Sum = {sum}')



'Goa Panjim' 'Andhra Amaravati' 'Kerala Tiruvanantapuram' 'Himachal Shimla'
states = []
capitals = list()