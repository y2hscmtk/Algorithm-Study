# https://www.acmicpc.net/problem/16724
'''
분리 집합
총 몇개의 그룹이 있는지 파악
그룹의 방향대로 순회하다가, 이미 방문한곳으로 이동하려는 순간을 SAFE ZONE으로 지정하면 됨
'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
data = [list(input()) for _ in range(N)]
visited = [[-1]*M for _ in range(N)] # 탐색 했는지 안했는지 여부
group_num,result = 0,0 # 그룹 식별자, 정답
dx = [0,0,-1,1]; dy = [-1,1,0,0] # 좌,우,상,하
dir = {"L":0,"R":1,"U":2,"D":3}

def find_group(x,y,group_num):
    global result
    if visited[x][y] != -1: # 이미 소속 그룹이 존재한다면 순환 종료
        if visited[x][y] == group_num: # 현재 식별자와 같다면 => 새로운 순환고리가 만들어짐
            result += 1 # 정답 + 1
        return
    visited[x][y] = group_num # 방문 처리
    nx = x + dx[dir[data[x][y]]]
    ny = y + dy[dir[data[x][y]]]
    find_group(nx,ny,group_num)
        
for x in range(N):
    for y in range(M):
        group_num +=1
        find_group(x,y,group_num)
print(result)