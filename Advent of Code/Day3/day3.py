def readData():
    with open('input.txt') as f:
        wire1 = f.readline().split(',')
        wire2 = f.readline().split(',')

        wire1[-1] = wire1[-1][:-1]
        wire2[-1] = wire2[-1][:-1]
    return wire1, wire2

def populatePath(wire):
    start = [0,0]
    stepsDict = dict()
    steps = 1
    for step in wire:
        direction = dirMappings[step[0]]
        moves = int(step[1:])
        for i in range(moves):
            start[0] += direction[0]
            start[1] += direction[1]
            stepsDict[tuple(start)] = steps
            steps += 1

    return stepsDict

'''
Have the paths for each wire.
Need to find all points of intersection and calculate Manhattan
distance from each.
Slightly brute force. Build set of (x,y) points for each wire.
Compute intersection of sets.
For each point in intersection, get manhattan distance from start.
Keep track of minimum.
Might be too big for memory. Lets see

Ok, it worked.
For Part2, instead of minimizing the Manhattan distance, we want to 
minimize the sum of steps each wire takes to get to an intersection point.
We return the intersection with the lowest such sum.

So in each simulation, we now keep a step counter which increments
after each step in any direction.
Obviously we cannot add to this to our tuple otherwise the intersection
set would be empty unless both wires reached the same point after
the same # of steps. (This is because it will hash all fields of the 
tuple)
Therefore, maybe build a dictionary for each position as well.
We hash on the position, and the value will be the # of steps to get there.
For each intersection point, we use each wire's hash table to get the
# of steps it took to get there.
Then we minimize the sum.
'''

wire1, wire2 = readData()
dirMappings = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}

wire1Dict = populatePath(wire1)
wire2Dict = populatePath(wire2)


minSum = 2e9
for point in wire1Dict:
    if point not in wire2Dict:
        continue
    stepsSum = wire1Dict[point] + wire2Dict[point]
    minSum  = min(minSum, stepsSum)
print(minSum)