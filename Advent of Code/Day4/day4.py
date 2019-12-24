import collections
minVal = 178416
maxVal = 676461

'''
Want to generate all passwords within the range that match the rule.
We can just brute force by checking every number in the range.
The other solution I am thinking of is some backtracking based solution.
However, I feel like just validating every number in the range will work
well enough


For part 2, the same digit cannot appear consecutively more than
twice.
Since we enforce the non decreasing rule first, we can be sure
that the digits are in sorted order.
From this point, its easy. Just count the # of occurrences of each digit.
If any of them appear more than twice, return false.
'''
def valid(num):
    rep = str(num) # Easier to work with string(list) then int.
    for i in range(1, len(rep)):
        if ord(rep[i]) < ord(rep[i-1]): # Checking non-decreasing rule
            return False
    counts = collections.Counter(rep)
    lastGroup = False
    for elem in sorted(counts):
        if counts[elem] == 2:
            lastGroup = True
    return lastGroup
ans = 0
for i in range(minVal, maxVal + 1):
    if valid(i):
        ans += 1
print(ans)