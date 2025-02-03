'''
1. 서로 다른 그래프 그룹의 개수 파악
2. 서로 다른 그래프 그룹을 최대 k개까지 연결 가능
3. 연결하는 과정에서 B가 포함된 그룹은 연결시키면 안됨
'''
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] # 간선 연결 정보
# 간선 정보
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

# 정점 A가 최대한 많은 정점과 연결, B가 포함된 그래프와는 연결 x
# 최대 K개의 그래프와 연결 가능 - 어떤 정점끼리 연결하는지는 상관없음 간선 하나만 존재하면 그래프 연결 가능하니까
A, B, k = map(int, input().split())
result = 0 # 최종 정점의 개수
# 1. 모든 정점에 대해서 BFS 실시 - 각 그래프 번호 설정
# 2. B가 포함된 그룹은 제외, 서로 다른 그래프 그룹에 대해서 가장 정점이 많은 순서대로 K개의 그래프를 연결한다고 생각
visited = [0 for _ in range(n+1)] # n개의 정점이 현재 어떤 그룹에 속해있는지 확인
disable_group = -1
a_group = -1
group_count = dict()

def bfs(start_node,code):
    global disable_group,a_group,result
    queue = deque()
    queue.append(start_node)
    visited[start_node] = code
    is_group_a = False
    count = 1 # 현재 그룹에 포함된 수 카운팅
    while queue:
        curr_node = queue.popleft()
        # A가 포함되어 있는 그룹인 경우 확인
        if curr_node == A:
            a_group = code # A가 포함된 그룹 번호 저장
            is_group_a = True
        # B가 포함되어 있는 그룹인 경우 확인 - 해당 그룹은 이후 누적 불가능하도록 벤 ㅓ리
        if curr_node == B:
            disable_group = code # 해당 코드 저장
        for node in graph[curr_node]:
            if visited[node] == 0: # 아직 그룹이 없다면
                visited[node] = code
                count += 1
                queue.append(node)
    if is_group_a:
        result += count
    group_count[code] = count # 해당 그룹에 총 몇개의 노드가 존재하는지 기록

# 모든 정점에 대해서 수행
group_code = 0
for node in range(1,n+1): # 1번 노드부터 n번노드까지
    if visited[node] == 0: # 아직 그룹이 확인되지 않은 노드 발견시
        group_code += 1 # 새로운 그룹
        bfs(node, group_code) # bfs 수행


# 최종 선별된 그룹들을 바탕으로 연결 가능한 그룹 추출 - 노드가 가장 많이 포함된 순서대로 추출
final = []
for group in group_count:
    if group != a_group and group != disable_group:
        final.append((group, group_count[group]))

final.sort(key=lambda x : x[1], reverse = True)

# 앞에서부터 k개만큼 더하기 가능
for i in range(k):
    if i < len(final):
        result += final[i][1]

print(result)