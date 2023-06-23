# https://www.acmicpc.net/problem/15651
from itertools import product
n, m = map(int, input().split())

data = [i for i in range(1, n+1)]
# product는 중복 순열 => repeat를 적어줘야함(그냥 적으면 에러남)
for array in product(data, repeat=m):
    print(*array)
'''
# 재귀함수를 이용한 풀이
n, m = map(int, input().split())

def nm(n, m, seq=[]):
    if len(seq) == m:
        print(" ".join(seq))
    else:
        for i in range(1, n+1):
            nm(n, m, seq+[str(i)])

nm(n, m)
'''