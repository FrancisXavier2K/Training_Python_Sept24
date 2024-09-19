
def calc(first_num : int, second_num : int) -> int:
    sum = first_num + second_num
    diff = first_num - second_num
    product = first_num * second_num
    quotient = first_num // second_num
    return sum, diff, product, quotient

s,d,p,q = calc(24,8)
print(s,d,p,q)
t1 = calc(35,7)
print(t1)
print(type(t1))
