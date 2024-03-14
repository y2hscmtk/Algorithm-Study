# https://www.acmicpc.net/problem/9466
'''
<아이디어>
dfs - 분리집합 응용
각 학생의 선호 학생이 '사이클'을 이루는 경우에만 팀이 될 수 있다.
사이클은 집합의 무작위 노드에서 출발해서 모든 노드를 순환할 수 있는 경우를 의미한다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

# 시작위치(start)로 다시 되돌아오는지 확인
def dfs(x):
    global result
    visited[x] = True # 방문처리
    cycle.append(x)
    num = parent[x]
    if visited[num]: # 방문처리 되어있다면
        # 해당 학생의 번호가 사이클에 포함되어있다면
        if num in cycle:
            result += cycle[cycle.index(num):] # 해당 학생의 번호 이후부터 모두 그룹으로 생성
        return
    else:
        dfs(num)

for _ in range(int(input())):
    n = int(input()) # 총 학생의 수
    parent = [0] + list(map(int,input().split()))
    # 모든 학생들의 선호 학생들을 순환하면서 그룹에 소속되는 학생이 몇명인지 파악
    visited = [False]*(n+1)
    result = []
    
    for i in range(1,n+1):
        if not visited[i]: # i번 학생이 아직 소속된 그룹이 없다면
            cycle = [] # 사이클이 만들어지는지 확인하기 위함
            dfs(i) # i번째 학생의 선호 학생을 바탕으로 dfs 시작 => 그룹이 만들어지는지 확인
    
    print(n - len(result)) # 소속된 팀이 없는 학생의 수 출력 