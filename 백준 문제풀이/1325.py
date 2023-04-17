# https://www.acmicpc.net/problem/1325

'''
첫째 줄에, N과 M이 들어온다. 
N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, 
"A가 B를 신뢰한다"를 의미한다. 
컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.
'''
from collections import deque
n, m = map(int, input().split())
# 0번째는 무시, 1번부터 N번까지
graph = [[] for i in range(n+1)]
result = [-1]  # 정답을 저장할 배열

# bfs


def bfs(i):
    queue = deque()
    queue.append(i)
    count = 0  # 방문한 노드의 수
    visited = [False for _ in range(n+1)]
    visited[i] = True
    while queue:
        node = queue.popleft()
        for e in graph[node]:
            if not visited[e]:
                visited[e] = True  # 방문처리
                count += 1
                queue.append(e)
    return count

    # 신뢰관계 입력받기
for i in range(m):
    a, b = map(int, input().split())
    # a가 b를 신뢰하면 b를 해킹하면 a를 해킹할수 있다.
    graph[b].append(a)

for i in range(1, n+1):
    result.append(bfs(i))

mc = max(result)
# 정답 출력
for i in range(1, len(result)):
    if result[i] == mc:
        print(i, end=' ')
