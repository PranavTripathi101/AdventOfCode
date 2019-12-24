import os, sys
sys.path.append(os.path.relpath('../'))
import computer

intcode = []
with open('input.txt') as f:
    intcode = [int(x) for x in f.read().split(',')]

comp = computer.Computer()
comp.solve(intcode)