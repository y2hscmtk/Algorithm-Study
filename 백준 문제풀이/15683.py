# https://www.acmicpc.net/problem/15683
'''
1. 각 감시모듈의 배열에 넣어놓고
2. 배열안의 모든 감시모듈에 대해서 방향을 바꿔가며 감시영역 설정과정 수행(수행 이전에 원본 배열을 저장)
3. 한 수행이 끝난뒤, 사각지대의 최소 영역을 갱신하고, 배열을 원래대로 되돌림

방향 처리
    0
    ^
3 <   > 1
    v
    2
방향 회전 => (x+1)%4 하면 90도 회전 처리

각 감쇠모듈별로, 현재 가리키고 있는 방향을 표현
'''
import sys
result = sys.maxsize
N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]  # 사무실 정보
copy_room = [r[:] for r in room]
# 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타냄

# 각 cctv가 바라볼수 있는 방향
cctv1 = [1]
cctv2 = [1, 3]
cctv3 = [0, 1]
cctv4 = [0, 1, 3]
cctv5 = [0, 1, 2, 3]

cctvies = [cctv1, cctv2, cctv3, cctv4, cctv5]

# 현재
cctv_see = []

# 위(0) 오른쪽(1) 아래(2) 왼쪽(3) 순으로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 최소값 갱신


def update():
    global result
    temp = 0
    for i in range(N):
        for j in range(M):
            if copy_room[i][j] == 0:
                temp += 1
    result = min(result, temp)


# 감시모듈의 위치를 기록할 배열
cctv_position = []
for i in range(N):
    for j in range(M):
        if 0 < room[i][j] < 6:
            cctv_position.append([i, j])  # cctv위치 삽입
            cctv_see.append(cctvies[room[i][j]-1][:])

# cctv의 개수가 한개도 없다면 안전영역을 출력하고 종료
if not cctv_position:
    update()
    print(result)
    sys.exit(0)


# 감시모듈 작동 => 모든 모듈의 방향 정보를 넣고, 감시모듈을 작동시킨다.
def start_cctv():
    global room, copy_room
    copy_room = [r[:] for r in room]  # 복사 => 원본배열을 손상시키기 않기 위해

    # cctv의 방향을

    # 모든 cctv마다 작동 시작
    for i in range(len(cctv_position)):
        # x, y = cctv_position[i]

        # 각 cctv가 관찰할수 있는 방향의 개수만큼
        for d in cctv_see[i]:
            x, y = cctv_position[i]
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                # 영역을 벗어나지 않는 경우에만 감시
                if 0 <= nx < N and 0 <= ny < M:
                    # 벽을 만났다면 이후의 영역에 대해선 감시 불가
                    if copy_room[nx][ny] == 6:
                        break
                    # 빈 칸을 만나면 #으로 변경(감시)
                    elif copy_room[nx][ny] == 0:
                        copy_room[nx][ny] = '#'
                    # 같은 cctv라면(0..<6) 당연히 위에 안걸리고 아래로(무시 처리)
                    # 좌표 이동
                    x = nx
                    y = ny
                else:
                    break
    # 모든 cctv에 대해서 탐색이 끝났다면 최소값 갱신
    update()


# 브루트포스
def run(index):
    # 모든 cctv의 방향을 설정했다면 작동 시작
    if index == len(cctv_position):
        start_cctv()
        return

    # count번째 cctv의 방향 변경
    for i in range(1, 5):
        for j in range(len(cctv_see[index])):
            cctv_see[index][j] = (cctv_see[index][j] + i) % 4

        run(index+1)
        # count번째 cctv의 방향 원래대로 변경
        for k in range(len(cctv_see[index])):
            cctv_see[index][k] = (cctv_see[index][k] - i) % 4


run(0)
print(result)
