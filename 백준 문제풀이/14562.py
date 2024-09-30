# https://www.acmicpc.net/problem/14562
'''
1. A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기이다. 하지만 상대 역시 3점을 득점하는 위험이 있다.
2. B는 1점을 얻는 연속 발차기이다.
현재 태균이의 점수 S와 상대의 점수 T가 주어질 때, S와 T가 같아지는 최소 연속 발차기 횟수를 구하는 프로그램을 만드시오.
'''
from collections import deque
def bfs(s, t):
    queue = deque()
    queue.append((s, t, 0))
    while queue:
        x, y, c = queue.popleft()
        # 두 수가 같아진 최소 순간
        if x == y:
            return c
        if x < y:  # x가 y보다 작을 때만 상태 추가
            # 1. 현재 점수만큼 점수를 얻는다. 상대도 3점을 획득한다.
            queue.append((x + x, y + 3, c + 1)) 
            # 2. 1점을 얻는다.
            queue.append((x + 1, y, c + 1))

for _ in range(int(input())):
    S, T = map(int, input().split())
    print(bfs(S, T))
