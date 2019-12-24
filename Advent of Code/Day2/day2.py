import os, sys
sys.path.append(os.path.relpath('../'))
import computer

intcode = []
with open('input.txt') as f:
    intcode = [int(x) for x in f.read().split(',')]

def findPair(intcode, comp):
    orig = intcode[:]
    for i in range(100):
        for j in range(100):
            intcode[1] = i
            intcode[2] = j
            comp.solve(intcode)
            if intcode[0] == 19690720:
                return(i,j)
            else:
                intcode = orig[:]


comp = computer.Computer()
orig = intcode[:]
print(findPair(intcode, comp))
