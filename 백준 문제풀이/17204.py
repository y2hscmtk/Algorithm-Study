# https://www.acmicpc.net/problem/17204
import sys
from collections import deque
n, k = map(int, input().split())  # n명이 게임 참가, 보영이는 k번
graph = [0]*n  # n명의 사람이 각각 누구를 가리키는지
for i in range(n):
    graph[i] = int(input())

# 만약 어떤 방법으로도 보성이가 걸리지 않는다면 -1을 출력한다.


def can_play():  # 먼저 0번에서 k번으로 가는 길이 있는지에 대해 탐색
    # 0번에서부터 탐색을 시작해서 k에 도달할때까지 얼마나 걸리는지
    queue = deque()
    queue.append(0)  # 0번부터 탐색 시작
    visited = [False]*(n)
    visited[0] = True  # 방문처리
    while queue:
        now = queue.popleft()  # 현재 누구인지
        next = graph[now]  # 다음 사람은 누구인지
        # k번에 도달하였다면 게임을 진행할 수 있다는 의미
        if next == k:
            return True
        if not visited[next]:
            visited[next] = True
            queue.append(next)
    # 다 돌았는데 True가 안걸렸다 => k로 갈 수 없다(게임불가)
    return False


if not can_play():
    print(-1)
    sys.exit(0)

queue = deque()
queue.append(0)  # 0번부터 탐색 시작
# 같은 사람을 여러명이 지목할수 있으므로(심지어는 자기자신 지목도 가능)
# 방문처리를 할 필요는 없다
count = 0
while queue:
    now = queue.popleft()  # 현재 누구인지
    count += 1  # 다음 사람을 부르면서 숫자를 외친다.
    next = graph[now]  # 현재 사람이 가리키고 있는 다음 사람
    if next == k:  # k를 찾았다면 count를 출력
        print(count)
        break
    queue.append(graph[now])  # 현재 사람이 가리키고 있는 사람
