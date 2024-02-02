
from collections import defaultdict

n = input("input positive number N: ")
n = int(n)
idxMap = defaultdict(int)
for i in range(1, n+1):
    cur = input("input a number: ")
    if cur not in idxMap:
        idxMap[cur] = i
x = input("input X to see its index: ")
if x in idxMap:
    print("The first appearence of number ", x, "is at index", idxMap[x])
else:
    print("-1")