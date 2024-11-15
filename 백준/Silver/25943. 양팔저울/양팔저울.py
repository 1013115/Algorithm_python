import sys
input = sys.stdin.readline

n = int(input())
pebbles = list(map(int, input().split())) 
s = [0, 0] 

for p in pebbles:
    if s[0] <= s[1]: 
        s[0] += p 
    else: 
        s[1] += p 

diff = abs(s[0]-s[1]) 
ans = 0 

while diff:
    for w in (100, 50, 20, 10, 5, 2, 1): 
        ans += diff//w # 
        diff %= w 
        
print(ans)