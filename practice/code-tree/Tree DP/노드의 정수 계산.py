# 트리 DP
'''
1번부터 n번까지의 노드
1번 노드가 루트 노드
1번 노드를 제외한 각 노드에는 정수가 존재

자신의 모든 자식 노드가 자신에게 값을 전파한 뒤에만 값을 전파할 수 있다.
적혀있는 수가 양수일 경우, 부모 노드에 자신의 값을 더한다.
적혀있는 수가 양수가 아닐 경우, 아무것도 하지 않는다.

다음과 같은 규칙으로 트리에 적혀있는 값들을 전파할 때, 최종적으로 1번 노드에 적히는 값

<DP를 사용하지 않을때>
모든 노드에 대해서(n) 최대 확인해야 하는 노드의 수가 n이므로 O(n^2)
<DP를 사용할 때>
dp[i] : i번 노드를 루트 노드로 하는 서브 트리에 있는 노드들의 전파값
O(n)으로 처리 가능 - 단말 노드를 만날 경우 반환(더 이상 자식 노드가 없을 때)
'''
n = int(input())
# 모든 정점의 방문 여부를 확인 하기 위한 배열 필요 - 단말 노드 판정시 사용
visited = [False]*(n+1)
value = [0]*(n+1)
graph = [[] for _ in range(n+1)]
dp = [None]*(n+1)

def dfs(node):
    # 이미 값이 기록된 경우 반환
    if dp[node] != None:
        return dp[node]
    visited[node] = True

    # 더 이상 자식 노드가 없는 경우 - 반환
    if not graph[node]:
        if value[node] > 0: # 양수인 경우는 반환
            dp[node] = value[node]
            return dp[node] 
        return 0

    # 해당 정점의 자식 노드에 대해서 dfs수행
    temp = 0
    for n in graph[node]:
        if not visited[n]: # 아직 방문하지 않은 자식인 경우만 생각
            temp += dfs(n) # 반환값 확인용
    dp[node] = temp + value[node] # 자식들의 반환값 + 자신의 값
    if dp[node] > 0:
        return dp[node]
    return 0


# 각 노드에 대한 정보
for i in range(2,n+1):
    t,a,p = map(int,input().split())
    # t가 1인 경우 +a
    if t == 0:
        a = -a
    # t가 0인 경우 -a
    # p는 해당 노드의 부모를 의미
    graph[p].append(i)
    value[i] = a # 값 저장

# 1번 노드에서 Tree - DP 수행
print(dfs(1))
