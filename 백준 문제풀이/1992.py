# https://www.acmicpc.net/problem/1992
'''
분할 정복
'''
N = int(input())
data = [list(map(int,input())) for _ in range(N)]

# 분할 정복 수행
def dfs(start,end,depth):
    # 현재 블럭에 대해서 모든 방향의 숫자 확인
    # 숫자가 모두 같은 경우, 해당하는 숫자 출력
    # 숫자가 다른 경우 깊이를 줄이고 각 방향에 대해서 dfs
    size = depth//2
    standard = data[start][end]
    for i in range(start,start+depth):
        for j in range(end,end+depth):
            if data[i][j] != standard:
                print("(",end='')
                # 각 모서리 블럭으로 dfs
                dfs(start,end,depth//2)
                dfs(start,end+size,depth//2)
                dfs(start+size,end,depth//2)
                dfs(start+size,end+size,depth//2)
                print(")",end='')
                return
    print(standard,end='')
    
dfs(0,0,N)