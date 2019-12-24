

with open('input.txt') as f:
    vals = [int(x) for x in f]

vals = list(map(lambda x: (x//3) - 2, vals))
sum = 0
for i in vals:
    while (i > 0):
        sum += i
        i = i // 3 - 2

print(sum)