# https://www.acmicpc.net/problem/1967

'''
트리(tree)는 사이클이 없는 무방향 그래프이다. 

트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 

트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 

이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.

이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 

정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 

아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.

트리의 노드는 1부터 n까지 번호가 매겨져 있다.
'''

'''
트리의 지름에 대한 이론 참고
https://blog.myungwoo.kr/112#comment18573031

1.시작 정점에서 가장 거리가 먼 정점을 구한다.
2.해당 정점에서 다시 거리가 가장 먼 정점을 구한다.
3.두 정점사이의 거리가 트리의 지름이 된다.
=> DFS를 2번 수행한다.
'''
# 재귀호출 가능횟수를 늘리기 위해 => RecursionError 방지
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
# 노드의 개수 n개
n = int(input())

# 트리로 이용할 리스트
tree = [[] for i in range(n+1)]

# 간선에 대한 정보 입력받기
for i in range(n-1):
    n1, n2, cost = map(int, input().split())
    # 양방향 트리이므로
    tree[n1].append([n2, cost])
    tree[n2].append([n1, cost])


# DFS를 통해 시작 정점에서 가장 멀리떨어진 정점 파악
# 각 정점에서 뻗어나가기 시작할때 길이를 누적시켜 저장
def DFS(start, d):
    for node, cost in tree[start]:
        # 아직 길이가 갱신되지 않았다면 => 아직 방문하지 않았다면
        if distance[node] == -1:
            # 길이 누적시켜 저장
            distance[node] = d + cost
            # 인정 정점에서 거리 누적시켜서 DFS
            DFS(node, d + cost)


# distance벡터 초기화
distance = [-1]*(n+1)
# 시작 정점에서의 코스트는 0으로 간주
distance[1] = 0
DFS(1, 0)  # 시작 정점에서 가장 멀리 떨어진 정점 찾기

# 가장 멀리 떨어진 정점의 인덱스 찾기
i = distance.index(max(distance))
# distance벡터 초기화
distance = [-1]*(n+1)
# 해당 인덱스에서 가장 멀리 떨어진 정점 찾기
distance[i] = 0
DFS(i, 0)

# 두 정점 사이의 거리가 정답이 된다.
print(max(distance))
