# https://www.acmicpc.net/problem/20924
'''
기가노드 : 루트 노드에서 순회를 시작했을 때, 처음으로 자식 노드가 $2$개 이상인 노드다
** 리포노드가 단 한개인 경우, 리프노드이자 기가노드가 된다. => 4-3-2-1 같은 경우
기둥 : 루트노드에서 기가노드까지다.
트리의 기둥과 가장 긴 가지의 길이를 측정하자.
기둥과 가지의 길이는 간선의 합이다.
** 루트 노드가 동시에 기가 노드인 경우도 가능하다.
0923/16:34 시작 16:57 1차 완료(테스트 케이스 오답) 16:59분 제출 오답
17:09
'''
import sys
sys.setrecursionlimit(10**6)
N,R = map(int,input().split()) # 노드의 개수, 루트 노드의 번호
tree = [[] for _ in range(N+1)] # 각 노드에 대한 연결정보
giga_node = R # 기가노드 번호 초기에는 루트노드와 동일하게 설정
branch_length = 0
for _ in range(N-1):
    a,b,d = map(int,input().split()) # a가 b와 연결되어있으며 간선의 길이가 d임을 의미
    tree[a].append((b,d)) # b와 연결되어있으며 간선 정보는 d임을 의미
    tree[b].append((a,d))

# 1. 루트 노드에서 기가노드까지의 거리 => 기둥의 길이 파악
# 2. 기가노드의 번호 파악 => 루트노드와 기가노드가 같은 경우 기둥의 길이는 0
# => dfs가 끝난 이후 리프노드가 단 한개인 경우, 리프노드가 동시에 기가노드가 된다.
def find_giga_node(n,length):
    global giga_node
    # 자식 노드가 최초로 1개가 아니게 되는 순간이 기가 노드를 발견한 순간이 될듯?
    # 1. 자식 노드가 1개인 경우 => 기둥이 진행중임을 의미함
    # 2. 자식 노드가 2개 이상인 경우 => 해당 노드까지가 기둥이며, 해당 노드가 기가노드가 됨
    # 3. 자식 노드가 없는 경우 => 기둥이 끝났으며, 해당 노드까지의 길이가 기둥임
    
    # 방문하지 않은 노드가 1개가 아닌 경우
    count = 0
    for b,d in tree[n]:
        if count>=2:
            giga_node = n
            return length
        if not visited[b]:
            count+=1
    if count == 0:
        giga_node = n
        return length
    # dfs 수행
    for b,d in tree[n]:
        if not visited[b]:
            visited[b] = True
            return find_giga_node(b,length+d)

# 가장 긴 가지의 길이 측정 dfs
# 3. 기가노드 존재하지 않을 경우, 가지 길이는 파악할 필요 없음 => 0
def find_long_branch(n,length):
    global branch_length
    
    # 더이상 자식 노드가 없다면 => 가지의 끝에 도달함
    count = 0
    for b,d in tree[n]:
        if not visited[b]:
            count += 1
    if count == 0:
        # 가지 최고길이 갱신
        branch_length = max(branch_length,length)
        return
    
    # 기가노드에 달린 노드들에 대해서 dfs 수행
    for b,d in tree[n]:
        if not visited[b]:
            visited[b] = True
            find_long_branch(b,length+d)

# 1. 기가노드 존재 유무 파악
visited = [False for _ in range(N+1)]
visited[R] = True
# 루트노드가 기가노드인지 아닌지 파악 필요
count = 0
for b,d in tree[R]:
    if not visited[b]:
        count+=1
if count != 1: # 루트노드가 기가노드인 경우
    wooden_pole = 0 
else:
    wooden_pole = find_giga_node(R,0) # 기둥의 길이

# 2. 기가노드 파악시 기가노드에서 가지 길이 파악
find_long_branch(giga_node,0)

print(wooden_pole,branch_length)
