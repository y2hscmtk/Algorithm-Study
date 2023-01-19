# https://www.acmicpc.net/problem/9372

'''
첫 번째 줄에는 테스트 케이스의 수 T(T ≤ 100)가 주어지고,

각 테스트 케이스마다 다음과 같은 정보가 주어진다.

첫 번째 줄에는 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 가 주어진다.
이후 M개의 줄에 a와 b 쌍들이 입력된다. a와 b를 왕복하는 비행기가 있다는 것을 의미한다. (1 ≤ a, b ≤ n; a ≠ b) 
주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.

테스트 케이스마다 한 줄을 출력한다.

상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수를 출력한다.
'''
import sys
sys.setrecursionlimit(10**4)  # 재귀가능횟수 확장

# 테스트 케이스의 수
t = int(input())

result = 0  # 정답을 출력할 변수


# DFS
def dfs(start):
    global result
    # 시장 정점 방문처리
    visited[start] = True
    result += 1  # 한 정점을 통과할때마다 +1
    # 인접 정점들을 대상으로 아직 방문하지 않았다면 DFS
    for node in graph[start]:
        if not visited[node]:  # 방문하지 않았다면
            dfs(node)  # 해당 정점을 기준으로 DFS


for _ in range(t):
    # n:정점의 개수(노드의 개수), m:간선의 개수
    n, m = map(int, input().split())
    # 그래프 초기화
    graph = [[] for _ in range(n+1)]
    # 출력값 초기화
    result = 0
    # 간선 정보 입력받기
    for i in range(m):
        # a와 b를 왕복하는 비행기 => 정점 a,b사이의 간선
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 입력받은 간선 정보를 바탕으로 알고리즘을 수행한다
    # => 모든 정점을 방문하는데 필요한 간선의 최소 개수
    # => 신장트리를 만들때 필요한 간선의 개수?

    # 방문배열 초기화
    visited = [False for _ in range(n+1)]
    # 1번 노드를 기준으로 dfs진행
    dfs(1)
    print(result-1)  # 시작노드를 방문할때도 +1되므로 -1하여 출력
