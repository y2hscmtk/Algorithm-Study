'''
같은 행에 1개의 퀸만 놓을 수 있음
같은 열에 1개의 퀸만 놓을 수 있음
행에 대해서, 왼쪽 오른쪽 대각선에 대해서 방문 배열 만들고 백트래킹
/ 방향 : row + col 일치      \ 방향 : row-col 일치
0 1 2                               0 -1 -2
1 2 3                               1  0  -1
2 3 4                               2  1  0
/ 방향 : (0+0) + (0+1) + .. + (N-1 + N-1) = 0,1,2,..,2N-2
\ 방향 : (0-(N-1)) + ... + ((N-1)-0) = -N+1,-N, .. , N-1 => 모든 칸에 N-1을 더해서 인덱스 0으로 시작 => 0,1,.. 2N-2
'''
def dfs(row):
    global result
    if row == N: # 마지막 행까지 도달하였다면 종료
        result += 1
        return
    for col in range(N):
        # 위, 오른쪽 위, 왼쪽 위 방문 정보 확인
        if not visited[col] and not diag1[row+col] and not diag2[row-col+N-1]:            
            visited[col] = True
            diag1[row+col] = True
            diag2[row-col+N-1] = True
            dfs(row+1) # 다음행에 대해서
            visited[col] = False
            diag1[row+col] = False
            diag2[row-col+N-1] = False

for i in range(1,int(input())+1):
    N = int(input())
    result = 0
    # / 방향 방문배열 초기화
    diag1 = [False]*(2*N-1)
    # \ 방향 방문배열 초기화
    diag2 = [False]*(2*N-1)
    # 열 방문 배열 초기화 
    visited = [False] * N
    dfs(0) # 0번째 행부터 시작
    print(f'#{i} {result}')