'''
배열 만들어 놓고 칠하기
현재 자신이 0이고 상하좌우 중 한곳이 1이라면 테두리
테두리 카운트 해서 출력
'''
dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = 0
board = [[0]*101 for _ in range(101)]

for _ in range(int(input())):
    s,e = map(int,input().split())
    # 채우기 시작
    for i in range(s,s+10):
        for j in range(e,e+10):
            board[i][j] = 1 # 채우기

# 몇개인지 카운팅
for i in range(101):
    for j in range(101):
        if board[i][j] == 1: # 0을 발견했고,상하좌우 중에 1이존재한다면
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0<=ni<101 and 0<=nj<101:
                    if board[ni][nj] == 0:
                        result+=1
                
                
print(result)