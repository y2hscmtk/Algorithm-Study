# https://www.acmicpc.net/problem/18290
'''
크기가 N×M인 격자판의 각 칸에 정수가 하나씩 들어있다. 
이 격자판에서 칸 K개를 선택할 것이고, 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 구하려고 한다. 
단, 선택한 두 칸이 인접하면 안된다. r행 c열에 있는 칸을 (r, c)라고 했을 때, (r-1, c), (r+1, c), (r, c-1), (r, c+1)에 있는 칸이 인접한 칸이다.
'''
import sys
def dfs(ci,cj):
    global result,select
    # 1. 종료조건 생각하기 : K개 골랐으면 종료
    if len(select) == K:
        # 1.2. 선택한 칸들이 서로 인접하면 안된다.
        for x,y in select: # 선택한 좌표들 중에서
            for nx,ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (nx,ny) in select: # 인접한 좌표가 존재한다면
                    return # 종료
        # 1.3. 선택한 수들을 더한 값들의 최대값 구하기
        temp = 0
        for x,y in select:
            temp += numbers[x][y]
        result = max(result,temp) # 더 큰수로 업데이트
        return
    
    # 2. 구간 생각 : NxM 크기의 격자판안의 모든 수
    if cj+1<M:
        cj+=1 # 다음 열
    else:
        if ci+1<N:
            ci+=1 # 다음 행
            cj=0 # 첫번째 열
        else: # 모든 행과 열을 다 살펴본것임
            return
    for i in range(ci,N):
        for j in range(cj,M):
            select.append((i,j))
            dfs(i,j)    
            select.pop() # 백트래킹
        cj = 0
        
select,result = [],-sys.maxsize
N,M,K = map(int,input().split())
numbers = [list(map(int,input().split())) for _ in range(N)] 
dfs(-1,M-1)
print(result)