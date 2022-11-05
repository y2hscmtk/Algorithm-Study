# 음료수 얼려 먹기

# N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우
# 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
# 다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

# 입력 조건
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다.
# 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

# 출력 조건
# 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

#n,m 입력받기
n, m = map(int,input().split())

#그래프 생성(얼음 틀)
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#붙어있는 0의 개수가 생성될 얼음의 개수가 될것
#모든 노드들을 DFS하여 count

def dfs(x,y):
    #x,y의 좌표가 영역을 벗어나면 바로 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않았다면~
    if graph[x][y]==0:
        #현재 노드를 방문처리
        graph[x][y]=1
        #재귀함수를 이용하여 상하좌우를 dfs로 탐색
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True #모든방향을 다 탐색후 True리턴 => 한번도 방문하지 않았던 노드에 방문했음을 의미
    return False #이미 방문한 노드일경우 False리턴

count = 0 
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count+=1

print(count)
    