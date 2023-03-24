# https://www.acmicpc.net/problem/1063
'''
킹은 상하좌우대각선 1칸씩 이동이 가능하다.
체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 
돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다.

입력
첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 
둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. 
N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.

출력
첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.
'''
# 알파벳은 열 정보를 의미함
dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

dict2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

# 바둑판 생성
board = [[0]*8 for _ in range(8)]

king, stone, n = list(input().split())

king_x, king_y = (8-int(king[1])), dict[king[0]]
stone_x, stone_y = (8-int(stone[1])), dict[stone[0]]

# 왕과 돌의 위치 설정
board[king_x][king_y] = 'k'
board[stone_x][stone_y] = 's'

'''
R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로
'''

move = {'R': [0, 1],
        'L': [0, -1],
        'B': [1, 0],
        'T': [-1, 0],
        'RT': [-1, 1],
        'LT': [-1, -1],
        'RB': [1, 1],
        'LB': [1, -1]}

# 움직임 입력받기
for _ in range(int(n)):
    command = input()
    # 왕 위치 변경
    knx = king_x + move[command][0]
    kny = king_y + move[command][1]
    # 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는
    if knx < 0 or knx >= 8 or kny < 0 or kny >= 8:
        continue  # 그 이동은 건너 뛰고 다음 이동을 한다.

    # 만약 이동하려는 자리에 이미 돌이 존재한다면
    if board[knx][kny] == 's':
        # 돌도 왕이 이동하려는 자리롤 이동시킨다.
        snx = stone_x + move[command][0]
        sny = stone_y + move[command][1]

        # 만약 돌의 다음 위치가 보드를 넘어가는 명령이라면 무시하고 다음명령부터
        if snx < 0 or snx >= 8 or sny < 0 or sny >= 8:
            continue  # 그 이동은 건너 뛰고 다음 이동을 한다.
        # 돌이 이동 가능하다면
        else:
            board[stone_x][stone_y] = 0
            stone_x, stone_y = snx, sny
            board[stone_x][stone_y] = 's'

    # 둘 다 문제없이 이동 가능하다면 이동을 수행한다.
    # 왕 이동
    board[king_x][king_y] = 0
    king_x, king_y = knx, kny
    board[king_x][king_y] = 'k'

print(dict2[king_y]+str(8-king_x))
print(dict2[stone_y]+str(8-stone_x))
