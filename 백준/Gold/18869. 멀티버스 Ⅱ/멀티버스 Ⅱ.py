import sys
input = sys.stdin.readline
from collections import defaultdict
import math

m, n = map(int, input().split())
universe = defaultdict(int)

def combinations_count(n, r=2):
    return math.comb(n, r)

for _ in range(m):
    # 행성 입력 받기
    planets = list(map(int, input().split()))
    
    # 행성 정렬 ( 구성 같은 행성 한개만 세기 )
    sortedPlanets = sorted(list(set(planets)))
    
    # 행성 순위 지정
    rank = {sortedPlanets[i] : i for i in range(len(sortedPlanets))}
    
    # 입력 받은 행성에 맞게 순위 저장
    vector = tuple([rank[i] for i in planets])
    
    # 해당 순위 벡터에 대한 개수 추가
    universe[vector] += 1
    
sum = 0

for i in universe.values():
    sum += combinations_count(i,2)
    
print(sum)