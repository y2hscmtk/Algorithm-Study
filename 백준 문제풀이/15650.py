# https://www.acmicpc.net/problem/15650
from itertools import combinations
n, m = map(int, input().split())
# 1부터 n까지의 수 배열 생성
number = [i for i in range(1, n+1)]
# number배열에서 중복없이 m개를 골라 출력
for i in combinations(number, m):
    print(*i)
