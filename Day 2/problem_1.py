
# Seperate states and capitals

import sys

states = []
capitals = []

for i in range (1, len(sys.argv)):
    argument = sys.argv[i].split()
    arguments = argument.split()
    states.append(arguments[0] )
    capitals.append(arguments[1])

print(states)
print(capitals)



