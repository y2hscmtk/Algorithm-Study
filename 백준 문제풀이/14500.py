# https://www.acmicpc.net/problem/14500
# https://www.acmicpc.net/problem/3019 문제 응용
# 브루트포스 => 모든 블럭을 각 자리에 한번씩 놓아보면서 조건을 만족하면 최대 숫자 갱신

# 회전 및 대칭시켜서 나올 수 있는 모양에 대한 모든 탐색 방향 정의

# 블럭의 모양에 대한 정의는 3019번의 블럭을 기준으로 작성함
# 1번째 블럭은 2가지 모양이 나올 수 있음
block1 = [[[1, 0], [2, 0], [3, 0]], [[0, 1], [0, 2], [0, 3]]]
# 2번째 블럭은 1가지 모양만 존재함
block2 = [[[1, 0], [0, 1], [1, 1]]]
# 3번째 블럭은 2가지 모양이 나올 수 있음
block3 = [[[0, 1], [-1, 1], [-1, 2]], [[1, 0], [1, 1], [2, 1]]]
# 4번째 블럭은 2가지 모양이 나올 수 있음
block4 = [[[0, 1], [1, 1], [1, 2]],
          [[-1, 0], [-1, 1], [-2, 1]]]
# 5번째 블럭은 4가지 모양이 나올 수 있음
block5 = [[[0, -1], [0, 1], [-1, 0]], [[0, -1], [0, 1], [1, 0]],
          [[-1, 0], [1, 0], [0, 1]], [[-1, 0], [1, 0], [0, -1]]]
# 6번째 블럭은 4가지 모양이 나올 수 있음
block6 = [[[0, 1], [0, 2], [-1, 2]], [[0, 1], [0, 2], [1, 0]],
          [[0, 1], [-1, 0], [-2, 0]], [[0, 1], [1, 1], [2, 1]]]
# 7번째 블럭은 4가지 모양이 나올 수 있음
block7 = [[[0, 1], [0, 2], [-1, 0]], [[0, 1], [0, 2], [1, 2]],
          [[0, 1], [-1, 1], [-2, 1]], [[0, 1], [1, 0], [2, 0]]]

# 만들어 질 수 있는 블럭들의 모든 탐색 방향을 소유
block_list = [block1, block2, block3, block4, block5, block6, block7]

n,m = map(int,input().split()) # 세로n, 가로m

graph = [list(map(int,input().split())) for _ in range(n)]

result = 0 # 테트로미노가 놓인 칸에 쓰인 수들의 최대값을 저장하기 위함


# 해당 좌표에 모든 블럭을 놓아보면서 영역을 벗어나지 않는지 검사
# 영역을 벗어나지 않는다면 블럭이 놓여진 칸의 숫자들을 모두 더해서 최대값 갱신
def put_block(i,j):
    global result
    # 해당 좌표에 놓아볼 블럭 결정
    for block in block_list:
        # 해당 블럭이 가진 모양들에 대해서(회전, 대칭)
        for block_position in block:
            point = graph[i][j] # 해당 블럭을 놓았을때 몇점의 포인트를 획득 가능한지 기록
            error = False
            for dx,dy in block_position: # 탐색 진행 방향
                # 블럭을 놓을 수 있는지 확인하기 위해
                nx = i + dx
                ny = j + dy
                # 해당 좌표가 영역을 벗어나지 않는다면
                if 0<=nx<n and 0<=ny<m:
                    point += graph[nx][ny] # 점수 더하기
                else: # 영역을 벗어난다면 해당 블럭은 현재 위치좌표에 완전히 놓을 수 없는 상황을 의미
                    error = True # 에러 처리
                    break # 더이상 탐색 진행 할 필요가 없음
            if not error: # 문제 없이 블럭을 다 놓았다면
                result = max(result,point) # 최고 점수 갱신

# 게임판에서 브루트포스 수행
for i in range(n):
    for j in range(m):
        # 해당 좌표에 블럭 놓기 시도
        put_block(i,j)


print(result)