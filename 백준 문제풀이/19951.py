# https://www.acmicpc.net/problem/19951
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
pSum = [0]*n
for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        pSum[i-1] += c
for i in range(len(data)):
    print(data[i]+pSum[i], end=' ')
