# https://www.acmicpc.net/problem/18917
'''
처음에 0이 하나 포함되어있는 배열 A가 있다. 이때, 다음 쿼리를 수행해야 한다.

1 x: A의 가장 뒤에 x를 추가한다.
2 x: A에서 x를 제거한다. A에 x가 두 개 이상 있는 경우에는 가장 앞에 있는 하나만 제거한다. 항상 A에 x가 있는 쿼리만 주어진다.
3: A에 포함된 모든 원소를 더한 값을 출력한다.
4: A에 포함된 모든 원소를 XOR한 값을 출력한다.
'''
import sys
input = sys.stdin.readline
# 쿼리의 개수
m = int(input())

a = [0]
xor = 0
sum_a = 0
for _ in range(m):
    op = list(map(int, input().split()))
    # A의 가장 뒤에 x를 추가한다.
    if op[0] == 1:
        sum_a += op[1]  # 합을 출력하기 위해
        xor ^= op[1]  # xor을 출력하기 위해
    elif op[0] == 2:
        sum_a -= op[1]  # 배열에서 하나 제거
        xor ^= op[1]
    # a의 합을 출력한다.
    elif op[0] == 3:
        print(sum_a)
    elif op[0] == 4:
        print(xor)
