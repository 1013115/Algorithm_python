# 차집합
import sys

input = sys.stdin.readline

a, b = map(int, input().split())

arr = set(map(int,input().split()))

brr = set(map(int,input().split()))
k =sorted(arr.difference(brr))
print(len(k))
print(' '.join(map(str,k)))