# https://www.acmicpc.net/problem/20364

# k번호의 왼쪽은 k+1, 오른쪽은 2k+1 인점을 이용,
# visited배열을 이용하여 선점한 땅 기록해두기
from collections import deque

visited = [] # 방문정보를 저장할 배열


def bfs(target):
    global visited
    queue = deque()    
    # bfs의 시작 노드는 1번
    queue.append(1)
    while queue:
        node = queue.popleft()
        # 목적지에 도달하기 전에 선점한 땅에 도달하였다면 해당 땅 번호 리턴
        if node//2 in visited:
            return node//2
        
        # 목적지에 도달하면 0리턴 => 해당 땅을 선점했다는 의미로 viisted배열에 삽입
        if node==target:
            visited.append(node)
            return 0
        
        # 이동 가능 노드는 2k,2k+1, 2가지 경우
        for next_node in (2*node,2*node+1):
            # n보다 작거나 같은 노드까지만 이동 가능(범위)
            if 0<=next_node<=n:
                queue.append(next_node)
            
    

n,q = map(int,input().split()) # n은 땅의개수(범위),q는 오리의 수(테스트 케이스의 수)
for i in range(q):
    target = int(input()) # i번째 오리가 가고싶어하는 목적지
    print(bfs(target)) # target에 도달할 수 있는지 없는지 여부 출력 