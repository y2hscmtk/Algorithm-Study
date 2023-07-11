# https://www.acmicpc.net/problem/17144
# 아래 과정을 T번 반복
# 1. 미세먼지 확산 => 현재 칸//5, 범위를 벗어나지 않고, 기계가 없는 공간이 아니면 상하좌우 이동,
# 1.1. 미세먼지 현황 업데이트 => 현재 칸 - 이동횟수*확산량
# 2. 공기청정기 작동 => 반시계 이동, 시계 이동 구현 => x1,x2,y1,y2 값 입력받아서 시계방향,반시계방향으로 회전하는 함수 작성
# 3. T초 후, 남아있는 미세먼지 총합 출력 => 총합 계산하는 함수 작성
R, C, T = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(R)]


# 현재 남아있는 미세먼지 총합 출력
def curr_dust():
    s = 0
    for i in range(R):
        for j in range(C):
            if dust[i][j] != -1:
                s += dust[i][j]
    return s


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 미세먼지 확산
def dust_move():
    global dust
    temp = [[0]*C for _ in range(R)]
    # 청소기가 있는 칸은 -1로
    temp[r1][c1] = -1
    temp[r2][c2] = -1
    '''
    (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    확산되는 양은 Ar,c/5이고 소수점은 버린다.
    (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다
    '''
    # 기존 좌표를 돌면서 먼지 발견시 상하좌우 이동 가능한지 검사
    for i in range(R):
        for j in range(C):
            if dust[i][j] > 0:  # 먼지라면
                count = 0
                # 상하좌우 검사
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    # 영역을 벗어나지 않으면서 공기청정기가 아니라면
                    if 0 <= nx < R and 0 <= ny < C and dust[nx][ny] != -1:
                        temp[nx][ny] += dust[i][j]//5
                        count += 1
                tmp = dust[i][j] - (count*(dust[i][j]//5))
                if tmp > 0:  # 음수의 경우 저장x
                    temp[i][j] += tmp
    dust = temp  # 원본 배열로 변경


# 먼지 상황 출력
def print_dust():
    print("-----------------------")
    for i in range(R):
        for j in range(C):
            print(dust[i][j], end=' ')
        print("")
    print("-----------------------")


# 반시계방향 먼지 청소(윗 부분)
def clean_ccw():
    global dust
    # 공기청정기 상단이 가장 위 인 경우 생각
    # => 마지막칸이 비어있지 않다면 더이상 순환하지 못함 + 나머지 세부분 생각할 필요 x
    if r1 == 0:
        if dust[r1][-1] == 0:
            pass
    else:
        # 순환 영역 4개로 나눠서 생각
        pass
    pass


# 시계방향 먼지 청소(아랫 부분)
def clean_cw():
    global dust
    # 공기청정기 상단이 가장 아래 인 경우 생각
    # => 마지막칸이 비어있지 않다면 더이상 순환하지 못함 + 나머지 세부분 생각할 필요 x
    if r2 == 0:
        # 마지막 칸이 비어있는지 검사
        if dust[r2][-1] == 0:
            pass
        pass
    else:
        # 순환 영역 4개로 나눠서 생각
        pass
    pass


machine = []
# 청소기가 있는 칸 파악해서 기록
c = 0
for i in range(R):
    for j in range(C):
        if dust[i][j] == -1:
            machine.append([i, j])
            c += 1
            if c == 2:
                break
    if c == 2:
        break
r1, c1 = machine[0]
r2, c2 = machine[1]

while T != 0:
    T -= 1  # 1초 경과
    # 미세먼지 확산
    dust_move()
    # 디버깅용
    # print_dust()
    # 공기 청정기 작동
    # 1. 반시계 작동(위쪽)
    clean_ccw()

    # 2. 시계 작동(아래쪽)
    clean_cw()
print(curr_dust())
