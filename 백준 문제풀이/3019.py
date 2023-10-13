# https://www.acmicpc.net/problem/3019

# 회전시켰을때 나올 수 있는 모든 탐색 방향에 대해 정의

# 1번째 블럭은 2가지 모양이 나올 수 있음
block1 = [[[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [0, 1], [0, 2], [0, 3]]]
# 2번째 블럭은 1가지 모양만 존재함
block2 = [[[0, 0], [1, 0], [0, 1], [1, 1]]]
# 3번째 블럭은 2가지 모양이 나올 수 있음
block3 = [[[0, 0], [0, 1], [-1, 1], [-1, 2]], [[0, 0], [1, 0], [1, 1], [2, 1]]]
# 4번째 블럭은 2가지 모양이 나올 수 있음
block4 = [[[0, 0], [0, 1], [1, 1], [1, 2]],
          [[0, 0], [-1, 0], [-1, 1], [-2, 1]]]
# 5번째 블럭은 4가지 모양이 나올 수 있음
block5 = [[[0, 0], [0, -1], [0, 1], [-1, 0]], [[0, 0], [0, -1], [0, 1], [1, 0]],
          [[0, 0], [-1, 0], [1, 0], [0, 1]], [[0, 0], [-1, 0], [1, 0], [0, -1]]]
# 6번째 블럭은 4가지 모양이 나올 수 있음
block6 = [[[0, 0], [0, 1], [0, 2], [-1, 2]], [[0, 0], [0, 1], [0, 2], [1, 0]],
          [[0, 0], [0, 1], [-1, 0], [-2, 0]], [[0, 0], [0, 1], [1, 1], [2, 1]]]
# 7번째 블럭은 4가지 모양이 나올 수 있음
block7 = [[[0, 0], [0, 1], [0, 2], [-1, 0]], [[0, 0], [0, 1], [0, 2], [1, 2]],
          [[0, 0], [0, 1], [-1, 1], [-2, 1]], [[0, 0], [0, 1], [1, 0], [2, 0]]]

block = [block1, block2, block3, block4, block5, block6, block7]

c, p = map(int, input().split())

height = list(map(int, input().split()))

result = 0


# 조건을 만족하는지 탐색
def check(copy_graph):
    global result
    # 조건을 만족한다면 result +=1
    # 모든 공백에 대해서, 위에 블럭이 없다면 성공
    # 블록들 중에서, 빈 공간인 좌표의 바로 위에 블록이 존재한다면 => 블럭을 잘못놓은것임
    for i in range(1, h):
        for j in range(c):
            if copy_graph[i][j] == False:  # 블럭이 없는데 => 즉 빈공간인데
                if copy_graph[i-1][j] == True:  # 위에는 블럭이 있다면
                    return False  # 블럭을 잘못 놓은것임
    return True  # 무사히 통과했다면 블럭을 잘 놓은것임


# 게임을 진행할 맵 만들기
# 세로로 세웠을때 가장 높은 막대의 높이는 4칸이므로
# max(hegith)+4 x c 크기의 맵을형성
h = max(height) + 4
graph = [[False]*c for _ in range(h)]  # 가로가 c이고, 높이가 h인 맵 형성
# 생성한 게임판에 정보 주입
for i in range(len(height)):  # 각 칸에 대한 높이 정보만큼 게임 맵에 표시
    count = height[i]
    # 높이만큼 True 표시
    for j in range(h-count, h):
        graph[j][i] = True


curr_block = block[p-1]
# 게임판에서 브루투포스 수행
for i in range(h):
    for j in range(c):
        # i,j가 블럭의 첫 부분에 해당하는 위치
        # 이번에 놓으려는 블럭의 방향정보에 대해서
        for block_position in curr_block:
            copy_graph = [g[:] for g in graph]
            # 해당 방향으로 블럭을 놓을 수 있는지 확인
            count = 0  # 블럭을 몇개 놓는데 성공했는지 => 모든 블럭은 4개의 작은 블럭임
            for x, y in block_position:
                nx, ny = i + x, j + y
                # 해당 좌표에 블럭을 놓았을때 설정한 게임판의 영역을 넘어서지 않는지 확인
                if 0 <= nx < h and 0 <= ny < c:
                    # 블럭을 놓을 수 있는 곳인지 확인
                    if copy_graph[nx][ny] == True:  # True라면 블럭을 놓을 수 없는 위치라는 것을 의미
                        break  # 해당 블럭은 못 놓는 것임
                    # 성공적으로 블럭을 놓는것에 성공
                    copy_graph[nx][ny] = True  # 블럭 놓기
                    count += 1
            # 블럭 4개를 모두 놓는데 성공했다면
            if count == 4:
                if check(copy_graph):  # 조건을 만족하는지 확인 => 공백 없이 설치했는지
                    result += 1  # 조건을 만족한다면 +1

print(result)
