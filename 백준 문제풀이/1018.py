# https://www.acmicpc.net/problem/1018

'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.

어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 

구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 

따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 

당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''
'''
2중 반복문을 통해 각 원소별로 돌아가면서 바둑판의 왼쪽 위 점을 정한후, 해당 점을 기준으로 8x8 영역이 되는 지점을 정해서
해당 영역안에서 뒤집기 알고리즘을 진행, 선정된 바둑판을 기준으로 2중반복문으로 상하좌우를 검사해서 모양이 모두 맞는지 확인하고 뒤집게 된다면
뒤집고, 횟수를 증가시킨다.
'''
import sys
import copy
n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

result = sys.maxsize  # 최소횟수를 기록하기위한 변수


# 방향벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 배열의 각 좌표별로 탐색
# 8x8크기로 자르기위해, 영역에서 벗아나는 지점은 고려하지않음
for i in range(n-7):
    for j in range(m-7):

        # 영역을 벗어나지않는다면 바둑판의 영역 지정
        board_n, board_m = i+8, j+8

        # 선택한 좌표를 기준으로 상하좌우 검사

        # 자기자신을 뒤집는 경우와, 자신의 주위를 뒤집는 경우중 최소값을 가려봐야함
        for l in range(2):
            # 원본바둑판 복사
            copy_board = copy.deepcopy(board)
            # 방문정보 초기화
            # 해당 좌표를 탐색하였는지여부를 기록하기 위한 배열
            visit = [[False]*m for _ in range(n)]
            if l == 0:
                count = 0  # 뒤집기 최소횟수 초기화
                for x in range(i, board_n):
                    for y in range(j, board_m):
                        # 체크대상
                        change = "W" if copy_board[x][y] == "B" else "B"
                        # 네 방향 탐색용
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            # 영역을 벗어나지 않는지 확인
                            if i <= nx < board_n and j <= ny < board_m:
                                # 모양이 같고, 한번도 안뒤집은 좌표라면(중복 뒤집기 방지)
                                if copy_board[nx][ny] == copy_board[x][y] and not visit[nx][ny]:
                                    copy_board[nx][ny] = change  # 뒤집기
                                    visit[nx][ny] = True  # 뒤집기 처리
                                    count += 1  # 뒤집기 횟수 증가
                # 탐색 종료후 count 최소횟수로 갱신
                result = min(result, count)
            else:
                # 바둑판 뒤집기 시작
                # 자기 자신을 뒤집고 시작
                copy_board[i][j] = "W" if copy_board[i][j] == "B" else "W"
                count = 1  # 뒤집기 최소횟수 초기화
                for x in range(i, board_n):
                    for y in range(j, board_m):
                        # 체크대상
                        change = "W" if copy_board[x][y] == "B" else "B"
                        # 네 방향 탐색용
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            # 영역을 벗어나지 않는지 확인
                            if i <= nx < board_n and j <= ny < board_m:
                                # 모양이 같고, 한번도 안뒤집은 좌표라면(중복 뒤집기 방지)
                                if copy_board[nx][ny] == copy_board[x][y] and not visit[nx][ny]:
                                    copy_board[nx][ny] = change  # 뒤집기
                                    visit[nx][ny] = True  # 뒤집기 처리
                                    count += 1  # 뒤집기 횟수 증가
                # 탐색 종료후 count 최소횟수로 갱신
            result = min(result, count)


print(result)
