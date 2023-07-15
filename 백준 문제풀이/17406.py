# https://www.acmicpc.net/problem/17406
import sys
from itertools import permutations
# 시간초과 날것같은데..

N, M, K = map(int, input().split())

# 배열의 모습
A = [list(map(int, input().split())) for _ in range(N)]

# 시행 가능한 연산의 수
op = [list(map(int, input().split())) for _ in range(K)]


result = sys.maxsize

# def check():
#     for t in temp_a:
#         print(*t)

# 위에서부터 시계방향으로 이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 배열 회전 함수
def rotate(r, c, s):
    # # 임시 배열 생성
    # temp_a = [a[:] for a in A]

    # 가장 왼쪽 윗 칸이 (r-s, c-s), 가장 오른쪽 아랫 칸이 (r+s, c+s)인 정사각형
    # 가장 바깥쪽 테두리부터, 안쪽 테두리까지 좁혀가기 => 테투리를 줄이면 될듯
    s_r, s_c = r-s-1, c-s-1
    e_r, e_c = r+s-1, c+s-1
    while True:
        direction = 0
        before = A[s_r][s_c]
        # 왼쪽 끝 좌표 설정
        x, y = s_r, s_c+1
        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 처음으로 되돌아 왔다면=>한바퀴 돌았다면 탈출
            if x == s_r and y == s_c:
                A[x][y] = before
                break
            # 각 테두리에서, 끝에 도달했다면 방향변경
            if nx < s_r or nx > e_r or ny < s_c or ny > e_c:
                direction += 1  # 방향 바꾸고
                continue
            # 오른쪽으로 한칸 이동
            A[x][y], before = before, A[x][y]
            # 이동 처리
            x = nx
            y = ny
        # 안쪽 칸으로 이동 => 더 이상 파고들수 없다면 종료
        s_r += 1
        s_c += 1
        if s_r == e_r and s_c == e_c:
            break
        e_r -= 1
        e_c -= 1
        if s_r == e_r and s_c == e_c:
            # for t in temp_a:
            #     print(*t)
            break


# 배열의 값 파악하는 함수
def update_min():
    global result
    for a in A:
        result = min(result, sum(a))


# 명령 수행 이전에, 기존 배열을 복사해둔다.
for array in permutations(op, K):
    save = [a[:] for a in A]
    for operation in list(array):
        r, c, s = operation
        rotate(r, c, s)
    # 최소값 갱신
    update_min()
    # 배열 원래대로 바꾸기
    A = [s[:] for s in save]

print(result)
