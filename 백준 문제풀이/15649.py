# https://www.acmicpc.net/problem/15649
from itertools import permutations
n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
for number in permutations(numbers, m):
    print(*number)
