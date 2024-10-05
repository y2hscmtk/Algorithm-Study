# https://www.acmicpc.net/problem/5587
import sys
n = int(input())
# 1~2n 이하의 카드
# n개의 카드는 상근이의 카드이며, 반드시 가장 낮은 수의 카드부터 낸다.
# 둘 중 한명이라도 카드를 전부 사용하면 게임이 종료된다.
# 게임 종료시 상대방이 가지고 있는 카드의 수를 점수로 획득한다.
card = [False for i in range(2*n+1)]
sangeun = [] # 상근이 카드 정보
enermy = [] # 상대 카드 정보

for _ in range(n):
    num = int(input())
    sangeun.append(num)
    card[num] = True

# 상대 카드 정보 갱신
for i in range(1,2*n+1):
    if card[i] == False:
        enermy.append(i)

# 게임은 상근이 부터 시작한다.
curr = -1
s,e = 0,0 # 잔여 카드량 확인
s_visited = [False for _ in range(n)]
e_visited = [False for _ in range(n)]
while True:
    # 현재 낼 수 있는 카드 중에서 가장 낮은 수의 카드를 낸다.
    # 상근이 부터 시작
    find = -1
    temp = sys.maxsize
    for i in range(n):
        if not s_visited[i]:
            # 기존에 고른 카드보다 수가 작으면서 현재 놓여져있는 카드보다 큰 수
            if curr < sangeun[i] and sangeun[i] <= temp:
                find = i
                temp = sangeun[i]
    if find != -1:
        curr = temp
        s_visited[find] = True
        s+=1
    else: # 찾지 못했다면 카드는 없어지고 상대의 턴으로 넘어간다
        curr = -1
    if s == n:
        print(n-e)
        print(0)
        break
    
    # 현재 낼 수 있는 카드 중에서 가장 낮은 수의 카드를 낸다.
    # 적의 차례
    find = -1
    temp = sys.maxsize
    for i in range(n):
        if not e_visited[i]:
            # 기존에 고른 카드보다 수가 작으면서 현재 놓여져있는 카드보다 큰 수
            if curr < enermy[i] and enermy[i] <= temp:
                find = i
                temp = enermy[i]
    if find != -1:
        curr = temp
        e_visited[find] = True
        e+=1
    else: # 찾지 못했다면 카드는 없어지고 상대의 턴으로 넘어간다
        curr = -1
    if e == n:
        print(0)
        print(n-s)
        break
    
