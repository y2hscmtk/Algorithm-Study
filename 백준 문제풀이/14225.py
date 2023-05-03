# https://www.acmicpc.net/problem/14225
from itertools import combinations
n = int(input())
s = list(map(int, input().split()))

candidate = []  # 집합으로 작성

# 1개부터 n+1개의 수 뽑기
for i in range(1, n+1):
    for select in combinations(s, i):
        candidate.append(sum(select))

candidate.sort()
numbers = set()
# 나올 수 없는 가장 작은 자연수 => 1부터 mad(candidate)+1까지의 수 중에서~
for i in range(1, candidate[-1]+2):
    numbers.add(i)
print(min(list(numbers - set(candidate))))
