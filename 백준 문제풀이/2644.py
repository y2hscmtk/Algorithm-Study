# https://www.acmicpc.net/problem/2644
'''
촌수계산

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 

이러한 촌수는 다음과 같은 방식으로 계산된다. 

기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 

예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
'''
from collections import deque
import sys
n = int(input())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
# 관계 표시를 위한 그래프
graph = [[] for _ in range(n+1)]

start, end = map(int, input().split())  # s와 e의 촌수를 계산

for _ in range(int(input())):
    s, e = map(int, input().split())
    # 관계 표현
    graph[s].append(e)
    graph[e].append(s)


meet = [-1]*(n+1)


def bfs():
    global result
    queue = deque()
    queue.append(start)  # 시작 노드
    meet[start] = 0  # 만남 처리
    while queue:
        people = queue.popleft()
        if people == end:  # 찾고자 하는 사람 발견시
            return meet[people]
        # 아직 발견하지 못했다면
        for next_people in graph[people]:
            if meet[next_people] == -1:  # 아직 만나지 않았다면
                meet[next_people] = meet[people] + 1  # 만남 처리
                queue.append(next_people)
    return -1


print(bfs())
# 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다
