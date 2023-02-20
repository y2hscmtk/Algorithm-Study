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
뒤집고, 횟수를 증가시킨다. => 오답처리
'''
'''
두번째 전략 : 왼쪽위가 하얀색으로 시작하는 바둑판과, 검은색으로 시작하는 바둑판 두가지를 미리 만들어놓고
좌표별로 두가지 경우를 모두 비교해서 최소값을 찾아내는 방법
'''
import sys
n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

result = sys.maxsize  # 최소횟수를 기록하기위한 변수

# 왼쪽위가 하얀색으로 시작하는 보드판
white = ["WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW", ]

# 왼쪽위가 검은색으로 시작하는 보드판
black = ["BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB"]


def white_board(i, j):
    # 해당 좌표를 기점으로 8x8공간의 배열의 값과 하얀색 보드판과 비교한다
    # 만약 값이 다르다면 count를 증가시킨다.
    count = 0
    for x in range(8):
        for y in range(8):
            if board[i+x][j+y] != white[x][y]:
                count += 1
    return count


def black_board(i, j):
    # 해당 좌표를 기점으로 8x8공간의 배열의 값과 하얀색 보드판과 비교한다
    # 만약 값이 다르다면 count를 증가시킨다.
    count = 0
    for x in range(8):
        for y in range(8):
            if board[i+x][j+y] != black[x][y]:
                count += 1
    return count


# 배열의 각 좌표별로 탐색
# 8x8크기로 자르기위해, 영역에서 벗아나는 지점은 고려하지않음
for i in range(n):
    for j in range(m):

        # 영역에서 벗어나면 다음좌표부터 진행
        if i+7 >= n or j+7 >= m:
            continue

        # 영역을 벗어나지않는다면 해당 좌표를 대상으로 왼쪽위가 하얀바둑판을 만들때와
        # 검은 바둑판을 만들때 두가지 경우를 검사하여 둘 중 최소값을 해당 좌표에 대한 최소값으로 지정
        # 이후 기존 최솟값과 비교하여 갱신한다.
        temp = min(white_board(i, j), black_board(i, j))
        result = min(result, temp)

print(result)
