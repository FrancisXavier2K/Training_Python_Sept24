
# Command line argument

import sys

states = []
capitals = list()

print(sys.argv)

for i in range(1, len(sys.argv)):
    arguments = sys.argv[i].split()
    states.append(arguments[0])
    capitals.append(arguments[1])

print(states)
print(capitals)