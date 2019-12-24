import collections
adjList = collections.defaultdict(list)
parList = collections.defaultdict(str)
with open('input.txt') as f:
    for line in f:
        parent, child = line[:-1].split(')')
        adjList[parent].append(child)
        parList[child] = parent

# Got the adjacency list.
# Now we do a preorder traversal starting at root (COM).
# Keep a running total which will track the orbits.

def countOrbits(current, nodesAbove):
    global orbits
    orbits += nodesAbove
    for child in adjList[current]:
        countOrbits(child, nodesAbove + 1)


'''
For part 2,
We need to find the shortest path from our orbit to santa's orbit.
This will require us to traverse up the tree. For this to work, each child needs to have a mapping
to its parent.
We can update the read function to support this. After this, we just do a BFS from our location until we find Santa.
After this, we might need to subtract 1 or 2 from the answer because the question does not want us to include the planet
we are orbiting and the planet Santa is orbiting.
'''

def getShortestPath(current, target):
    q = collections.deque()
    q.append([current, 0])
    visited = set({current})
    while q:
        curPlanet, curSteps = q.popleft()
        if curPlanet == target:
            return curSteps - 2
        visited.add(curPlanet)
        for planet in adjList[curPlanet]:
            if planet not in visited:
                q.append([planet, curSteps + 1])
        if parList[curPlanet] not in visited:
            q.append([parList[curPlanet], curSteps + 1])
    return -1

orbits = 0
countOrbits('COM', 0)

print(getShortestPath('YOU', 'SAN' ))