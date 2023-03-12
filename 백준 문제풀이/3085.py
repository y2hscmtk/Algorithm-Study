# https://www.acmicpc.net/problem/3085
'''
문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 

그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
'''
# 보드의 크기
n = int(input())
# 사탕 정보
candy = [list(input()) for _ in range(n)]
# 상근이가 먹을수 있는 사탕의 최대 개수
max_count = 0  # 하나도 못먹는 경우는 없을테니, 0이 최소인 경우가 된다.

# 2. 모두 같은색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.(개수를 센다.)


def calc_max_count():
    global max_count
    # 사탕배열을 돌면서 각 행,열에서 연속된 사탕의 수 파악

    # 행 검사
    for x in range(n):
        curr_candy = candy[x][0]
        temp = 1  # 임시 카운트
        for y in range(n-1):
            if curr_candy == candy[x][y+1]:
                temp += 1  # 일치할경우 개수 증가,
            else:  # 일치하지 않을경우
                curr_candy = candy[x][y+1]  # 다음 사탕으로 전환
                max_count = max(max_count, temp)  # 최대값 갱신
                temp = 1  # 임시 카운트 초기화
        max_count = max(max_count, temp)  # 최대값 갱신

    # 열 검사
    for y in range(n):
        curr_candy = candy[0][y]
        temp = 1  # 임시 카운트
        for x in range(n-1):
            if curr_candy == candy[x+1][y]:
                temp += 1  # 일치할경우 개수 증가,
            else:  # 일치하지 않을경우
                curr_candy = candy[x+1][y]  # 다음 사탕으로 전환
                max_count = max(max_count, temp)  # 최대값 갱신
                temp = 1
        max_count = max(max_count, temp)  # 최대값 갱신


    # 1. 상근이는 사탕의 색이 다른 인접한 두 칸을 고르고, 서로 교환한다.
for i in range(n):
    for j in range(n):
        # 인접한 영역은 오른쪽 값과 아래쪽 값으로 규정(반복을 통해 모두 비교하게 됨)
        # 영역을 벗어나지 않는지 확인
        if 0 <= i+1 <= n-1:  # 행 영역이, 영역을 벗어나지 않으면 비교 가능(값이 존재하므로)
            # 아래로 인접한 값과 현재 값이 다른지 확인
            if candy[i][j] != candy[i+1][j]:
                # 값이 다르다면 서로 값을 교환한다음, 가장 긴 사탕의 개수 파악
                candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
                calc_max_count()
                # 사탕위치 다시 원위치
                candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]  # 백트래킹
        # 열 영역이 영역을 벗어나지 않으면 비교가능
        if 0 <= j+1 <= n-1:
            # 오른쪽으로 인접한 값과 현재 값이 다른지 확인
            if candy[i][j] != candy[i][j+1]:
                # 값이 다르다면 서로 값을 교환한다음, 가장 긴 사탕의 개수 파악
                candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
                calc_max_count()
                # 사탕위치 다시 원위치
                candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]  # 백트래킹

# 3. 상근이가 먹을수 있는 사탕의 최대 개수를 구하라
print(max_count)
