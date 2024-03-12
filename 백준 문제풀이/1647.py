# https://www.acmicpc.net/problem/1647
'''
아이디어
2개의 분리집합으로 나누기
=> 크루스칼 or 프림 알고리즘으로 MST 찾은 다음, MST에서 가장 길이가 긴 간선을 제거
=> '마을에는 집이 하나 이상 있어야 한다.' 다시 말하면 집이 하나라도 있으면 마을 취급
=> 길이가 가장 긴 간선을 제거하면 노드 하나가 독립되고 마을 하나가 더 생긴다.
첫째 줄에 없애고 남은 길 유지비의 합의 최솟값을 출력한다.

크루스칼
1. 간선들을 최소힙에 삽입한다. => 오히려 더 시간이 많이 걸릴 수 있다.
2. 해당 간선을 이음으로서 순환고리가 만들어지는지 확인한다. => 분리집합
3. 순환고리가 만들어지지 않는다면 간선 채택 가능, 순환고리가 만들어진다면(부모가 같다면) 채택 불가능
'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split()) # 집(노드)의 개수, 길(간선)의 개수
parent = list(range(N+1)) # 집은 1번부터 시작
result = 0 # 길 유지비용의 최소값

# 부모 찾기
def find(x):
    if x!=parent[x]: # 자기 자신이 부모가 아니라면 => 더 부모가 있음
        parent[x] = find(parent[x]) # 현재 x가 부모로 삼고 있는 노드의 부모 가져오기(축약)
    return parent[x] # 부모 반환

queue = [] # 최소 힙으로 사용하기 위함
for _ in range(M):
    a,b,cost = map(int,input().split())
    queue.append((cost,a,b))

max_length = -1 # 만들어진 집합에서의 가장 큰 비용을 의미하는 간선
queue.sort() # 오름차순 정렬
for cost,a,b in queue:
    a_parent = find(a); b_parent = find(b)
    if a_parent != b_parent: # 두 부모가 같지 않다 => 서로 다른 집합이다 => 사이클이 만들어지지 않는다.
        # 두 집합을 하나의 집합으로 만들기 => 부모 바꾸기
        if a_parent < b_parent:
            parent[b_parent] = a_parent
        else:
            parent[a_parent] = b_parent
        result += cost # 최소 비용 더하기
        # max_lenght = max(max_lenght,cost) # 현재 그룹에서의 최대 비용 업데이트
        max_length = cost # 어차피 오름차순 정렬 돼있음
print(result-max_length) # 최대길이 제거