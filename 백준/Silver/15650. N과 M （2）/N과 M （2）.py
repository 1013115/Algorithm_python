import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())

num = [i for i in range(1,n+1)]

ans = combinations(num,m)
for a in ans:
    print(*a)
    