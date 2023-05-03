# https://www.acmicpc.net/problem/14225
from itertools import combinations
n = int(input())
s = list(map(int, input().split()))

visited = [False] * (20 * 100000)

# 1개부터 n+1개의 수 뽑기
for i in range(1, n+1):
    for select in combinations(s, i):
        visited[sum(select)] = True

# 방문처리가 안돼있는 수가 최소값
for i in range(1, len(visited)):
    if not visited[i]:
        print(i)
        break
