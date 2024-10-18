# https://www.acmicpc.net/problem/18115
'''
1. 제일 위의 카드 1장을 바닥에 내려놓는다.
-> 가장 밑의 수를 현재 기준 가장 앞에 둔다.
2. 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
-> 가장 밑의 수를 현재 기준 앞에서 두번째에 둔다.
3. 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
-> 가장 밑의 수를 현재 기준 가장 아래에 둔다.

카드가 2장 이상일 때만 쓸 수 있다는 조건은 An이 항상 1이므로 보장되어있음
1,2,... N에서 위 연산을 거꾸로 수행

풀이참조 O
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
a.reverse() # 명령 역산 ; 가장 맨 위의 1은 가장 마지막 명령을 수행했을 것이므로

dq = deque()
# 1부터 N까지에 대해 역산
for i in range(N):
    if a[i] == 1: # 가장 앞에 둔다
        dq.appendleft(i + 1)
    elif a[i] == 2: # 앞에서 두번째에 둔다
        dq.insert(1, i + 1)
    elif a[i] == 3: # 맨 밑에 둔다
        dq.append(i + 1)

print(*dq)
