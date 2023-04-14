# https://www.acmicpc.net/problem/1996
n = int(input())

graph = [list(input()) for _ in range(n)]
new = [[0]*n for _ in range(n)]

# 상하좌우, 대각선까지 커버해야함
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


# 입력받은 좌표의 상하좌우에 값을 누적하여 더해줌
def change(x, y):
    z = int(graph[x][y])
    # 지뢰가 있다는 표시로 값을 변경해줌
    new[x][y] = '*'
    # 상하좌우에 값 더하기
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 맵 범위를 벗어나지 않으면서
        # M으로 표시되지 않은 공간인 경우에만 값을 더해준다.
        if 0 <= nx < n and 0 <= ny < n and new[nx][ny] != 'M':
            # 지뢰가 아닌지도 확인해야함
            if new[nx][ny] != '*':
                # 값 더해주기
                new[nx][ny] += z
                # 값을 더해서 10을 넘어간다면 M으로 변경
                if new[nx][ny] >= 10:
                    new[nx][ny] = 'M'


# 맵을 기준으로 지뢰의 상하좌우좌표에 지뢰에 적힌 숫자만큼 더해주고,
# 값이 10이상인지 확인하여 10을 넘겼다면 M으로 변경한다.
for i in range(n):
    for j in range(n):
        # .이 아닌 문자, 즉 숫자를 만났다면
        if graph[i][j] != '.':
            change(i, j)

for i in range(n):
    for j in range(n):
        print(new[i][j], end='')
    print('')
