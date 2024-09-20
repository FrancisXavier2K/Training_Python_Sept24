
# Slicing


place = 'bengaluru'

place2 = place[:]
print(place2)

place2 = place[::]
print(place2)

place2 = place[:5]
print(place2)

place2 = place[5:]
print(place2)

place = 'bengaluru'
print(place[1:9])
print(place[1:19])
print(place[-2:9])
print(place[1:9:2])
print(place[10:1:-2])
print(place[-2:1:-2])
print(place[-1::-1])
print(place[::-1])