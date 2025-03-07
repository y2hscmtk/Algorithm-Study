'''
트리 노드 제거
트리에서 노드 하나를 지운다 -> 자손도 같이 지워진다.
지워진 잏후 트리에서의 리프 노드의 개수를 구하라
'''
n = int(input())

leaf_node = 0
root = -1

# 각 노드의 부모 정보
parent = list(map(int,input().split()))
graph = [[] for _ in range(n)]
removed = [False]*(n)


for i in range(n):
    x,y = i,parent[i]
    if y == -1:
        root = x
        continue
    graph[y].append(x) # 부모 -> 자식 경로 생성
    
remove_node = int(input())


# 아직 방문되지 않은 정점들 방문하며 리프 노드 수 파악
def dfs(curr_node):
    global leaf_node
    # 현재 노드가 제거된 경우 스킵
    if removed[curr_node]:
        return

    # 현재 노드가 리프 노드인지 판단
    is_leaf = True
    for node in graph[curr_node]:
        if removed[node]:
            continue
        dfs(node)
        is_leaf = False
    
    if is_leaf:
        leaf_node += 1

removed[remove_node] = True # 방문 처리 - 삭제 처리
dfs(root)
print(leaf_node)