# 트리 전달
'''
연산 i w : i번 노드에서 점수 w 획득, 이후 i번 노드의 자식노드들에 대해서도 같은 연산 수행
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n,m = map(int,input().split())
# 각 노드의 부모 노드 - 1번이 루트 노드
parent = [0] + list(map(int,input().split()))
dp = [0]*(n+1)
graph = [[] for _ in range(n+1)]

# 간선 정보 생성
for i in range(1, n+1):
    x = parent[i]
    if x == -1:
        continue
    graph[x].append(i) 

for _ in range(m):
    x,y = map(int,input().split())
    dp[x] += y # 부모 초기 점수값 설정

# = 루트노드의 노드의 수를 구하는 것과 같은 문제
def dfs(root):
    # 모든 자식에 대해서
    for node in graph[root]:
        dp[node] += dp[root] # 부모가 갖고 있는 점수를 자식에도 모두 전파
        dfs(node)

dfs(1)

print(*dp[1:])