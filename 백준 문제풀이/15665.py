# https://www.acmicpc.net/problem/15665
from itertools import permutations
n, m = map(int, input().split())
# m개를 뽑아서 배열을 만들것
array = list(map(int, input().split()))
# 같은수를 최대 m개 뽑을수 있다는 의미이므로
# array를 m배 한 배열에서 permutaion을 이용
array *= m

result = set()

for extract in permutations(array, m):
    result.add(extract)

result = list(result)

result.sort()  # 오름차순 정렬

for data in result:
    print(*data)
