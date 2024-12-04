# 빨R -> 초G, 초G-> 파B, 파B->빨R
# greedy

import sys
input = sys.stdin.readline

n = int(input().strip())  # 입력값에서 불필요한 공백 제거

arr = input().strip()
arr=list(arr)
change = {'R': 'G', 'G': 'B', 'B': 'R'}

def change_light(idx, arr):
    
    """arr.replace(arr[idx],change[arr[idx]])
    arr.replace(arr[idx+1],change[arr[idx+1]])
    arr.replace(arr[idx+2],change[arr[idx+2]])"""
    arr[idx], arr[idx + 1], arr[idx + 2] = change[arr[idx]], change[arr[idx + 1]], change[arr[idx + 2]]
    return arr


def solve(new_arr):
    count = 0
    
    if len(new_arr) < 3:
        return float('inf')

    for i in range(1, len(new_arr) - 2):
        while new_arr[0] != new_arr[i]:
            count += 1
            new_arr = change_light(i, new_arr)

    if new_arr[0] == new_arr[-1] == new_arr[-2]:
        return count
    return float('inf')



answer = float('inf')


for i in range(3):
    answer = min(answer, solve(arr.copy()) + i)
    arr = change_light(0, arr)

if answer == float('inf'):
    answer = -1
print(answer)
