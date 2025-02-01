# https://www.acmicpc.net/problem/1018
'''
1. 8x8크기의 영역을 나눈다.
2. 나눠진 영역을 선택하였을 때, 잘못 칠해진 체스판의 수를 카운팅
3. 업데이트
'''
# 비교용
white = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
black = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]

def update(x,y):
    w,b = 0,0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if board[i][j] != white[i-x][j-y]:
                w+=1
            if board[i][j] != black[i-x][j-y]:
                b+=1
    return min(w,b) # 최소 변경 횟수 반환

# 보드판의 시작 지점 선택
min_count = float('inf')
for i in range(n-8+1):
    for j in range(m-8+1):
        min_count = min(min_count,update(i,j))

print(min_count)