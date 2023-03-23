# https://www.acmicpc.net/problem/1388
'''
가로로 연속된 -는 1개의 타일로 취급
세로로 연속된 |는 1개의 타일로 취급
총 몇개의 타일이 필요한지 카운팅
'''
# 세로, 가로
n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

result = 0  # 총 타일의 개수


# 가로 줄 탐색
def check_width(i, j):
    for k in range(j, m):
        # -마크라면 확인처리
        if board[i][k] == '-':
            board[i][k] = 'x'  # 확인처리
        # 다른 문양을 만난다면, 반복 종료
        else:
            return


# 세로 줄 탐색
def check_height(i, j):
    for k in range(i, n):
        # +마크라면 확인처리
        if board[k][j] == '|':
            board[k][j] = 'x'  # 확인처리
        # 다른 문양을 만난다면, 반복 종료
        else:
            return


# 가로 타일 카운팅
for i in range(n):
    for j in range(m):
        # 아직 확인하지 않은 곳중에 최초로 -문양을 방문했다면 result+1하고
        # 오른쪽 방향 쭉 확인
        if board[i][j] == '-':
            check_width(i, j)
            result += 1
        # 아직 확인하지 않은 곳중에 최초로 +문양을 방문했다면 result+1하고
        # 아래쪽 방향 쭉 확인
        elif board[i][j] == '|':
            check_height(i, j)
            result += 1

print(result)
