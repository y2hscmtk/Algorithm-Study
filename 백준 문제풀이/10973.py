# https://www.acmicpc.net/problem/10973
from itertools import permutations
'''
만들 수 있는 모든 경우의 수를 배열에 저장 후 정렬
배열에 저장된 수를 돌다가 주어진 배열과 같은 수 발견시, 이전 수 출력
사전순으로 가장 처음에 오는 순열인 경우에는 -1을 출력한다.
'''
n = int(input())
numbers = [i for i in range(1, n+1)]
array = list(map(int, input().split()))
# 이전수 기록용 배열 last => 초기 값은 가장 처음 값으로 지정
last = [*numbers]
# 만들 수 있는 모든 경우의 수에 대해
for i, a in enumerate(permutations(numbers, n)):
    # permutations에 의해 결과물은 오름차순으로 정렬됨
    if list(a) == array:  # 찾고자 하는 배열과 동일한 값 발견시
        # 사전순으로 가장 처음에 오는 순열인지 확인(인덱스가 0인지 확인)
        print(-1) if i == 0 else print(*last)
        break
    last = [*a]  # 현재 값 저장
