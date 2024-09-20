
# find method


place = 'shivamogga'

print(place.index('shiva')) # 0
print(place.index('mogga')) # 5
print(place.index('mogga', 2)) # 5
#print(place.index('mogga', 2, 7)) # -1
print(place.index('mogga', 4, 10)) # 5
#print(place.index('mogga', 4, 9)) # -1
#print(place.index('kerala', 0, 10)) # -1

print(place * 3)