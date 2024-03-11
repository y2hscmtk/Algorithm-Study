# https://www.acmicpc.net/problem/20040
'''
사이클이 발생하였는지 파악
'순환'해야지 사이클임
분리집합을 이용해서 부모 노드가 같다면 사이클이 발생한 것이며, 부모 노드가 같지 않다면 서로 다른 그룹이므로 합친다.
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split()) # n 정점의 개수, m 간선의 개수
parent = [i for i in range(n)]# 부모 노드 => 0부터 시작, 시작 시점에서는 자기 자신이 루트

# union-find
def find(x):
    if x != parent[x]: # 자기 자신의 인덱스와 같지 않다면 아직 부모를 못 찾은것
        parent[x] = find(parent[x])
    return parent[x]
    
for i in range(m): # 간선의 개수만큼 반복
    a,b = map(int,input().split())
    a_parent = find(a)
    b_parent = find(b)
    # 두 노드에 대한 집합이 서로 같지 않다면 => 합치더라도 사이클이 만들어 지지 않음
    if a_parent != b_parent:
        if a_parent < b_parent:
            parent[b_parent] = a_parent
        else:
            parent[a_parent] = b_parent
    else: # 두 노드가 속한 집합이 같다면 => 합치면 사이클이 만들어 진다.
        print(i+1) # 몇번째에서 사이클이 만들어 졌는지 출력
        sys.exit(0)
print(0) # 사이클이 만들어 지지 않는다.