
my_str = ''

for count in range(1, 14):
    my_str = my_str + 'T' + str(count) + ':\n\n'

fptr = open('case_study_teams.txt', 'w')
fptr.write(my_str)
fptr.close()


try:
    nithin = print('Nithin') # print() returns nothing
    print(nithin) #None
    print(len(nithin)) # causes exception
except TypeError as exp:
    print('Some Error Occured')
    print(exp)

#TypeError: object of type 'NoneType' has no len()


