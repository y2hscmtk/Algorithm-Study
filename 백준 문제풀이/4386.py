# https://www.acmicpc.net/problem/4386
'''
1. 각 좌표들을 입력받는다.
2. 모든 좌표들에 대해서 간선 정보 만들기
만들 수 있는 간선은 최대
100 + 99 + .. + 2 + 1 = 5050개
크루스칼 알고리즘 수행
'''
from math import sqrt
n = int(input())
star = [[] for _ in range(n)]
parent = [i for i in range(n+1)] # 각 그룹의 root 노드
for i in range(n):
    star[i] = list(map(float,input().split()))
# 간선 정보 만들기
edges = []
for i in range(n-1):
    x1,y1 = star[i]
    for j in range(i+1,n):
        # 두 정점 사이의 거리 구하기
        x2,y2 = star[j]
        cost = sqrt((x2-x1)**2 + (y2-y1)**2)
        edges.append((cost,i,j))

def find_parent(x):
    if x!=parent[x]: # 루트노드가 아니라면(자기 자신의 번호와 인덱스가 같은 경우 루트 노드)
        parent[x] = find_parent(parent[x])
    return parent[x] # 루트노드라면 리턴

# 최단 거리 순으로 갱신
edges.sort()
# 크루스칼 알고리즘 수행
result = 0
for cost,x,y in edges:
    # 두 정점 x,y가 다른 집합에 속해있는지 확인
    x_parent = find_parent(x)
    y_parent = find_parent(y)
    if x_parent != y_parent: # 서로 다른 집합에 속해있다면(두 정점을 잇더라도 환영고리가 만들어지지않음)
        # 집합 합치기(부모 노드는 작은 번호 순으로 쳬택)
        if x_parent < y_parent:
            parent[y_parent] = x_parent
        else:
            parent[x_parent] = y_parent
        result += cost # 간선 잇기
print(round(result,2))
