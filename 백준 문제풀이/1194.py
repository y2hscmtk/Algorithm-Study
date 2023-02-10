# https://www.acmicpc.net/problem/1194

'''
민식이는 지금 미로 속에 있다. 미로는 직사각형 모양이고, 여행길을 떠나기 위해 미로를 탈출하려고 한다. 미로는 다음과 같이 구성되어져있다.

빈 칸: 언제나 이동할 수 있다. ('.')
벽: 절대 이동할 수 없다. ('#')
열쇠: 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. ('a', 'b', 'c', 'd', 'e', 'f')
문: 대응하는 열쇠가 있을 때만 이동할 수 있다. ('A', 'B', 'C', 'D', 'E', 'F')
민식이의 현재 위치: 빈 곳이고, 민식이가 현재 서 있는 곳이다. ('0')
출구: 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. ('1')
달이 차오르는 기회를 놓치지 않기 위해서, 미로를 탈출하려고 한다. 한 번의 움직임은 현재 위치에서 수평이나 수직으로 한 칸 이동하는 것이다.

민식이가 미로를 탈출하는데 걸리는 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.
'''
'''
아이디어 : 열쇠를 갖고있는 경우에 한해서 출입이 가능해야하므로, 큐에 데이터를 넣을때 열쇠 보유여부도 함께 보낸다.
좌표 방문시 현재 보유중인 열쇠목록을 확인하고 열쇠를 보유하고 있다면 방문한다.
열쇠를 획득하면 갔던길을 다시 되돌아갈수 있도록 한다.
'''
from collections import deque
n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

found = False
# 탐색 시작좌표(0) 찾기
for i in range(n):
    if not found:
        for j in range(m):
            if graph[i][j] == '0':
                s, e = i, j  # 탐색 시작 좌표 기록
                found = True
                break

# 각 문에 대한 코드 번호를 부여
door = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
key = {'a': 0, 'a': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
# key[door['A']]를 통해, 현재 키가 보유중인지 여부를 확인할수 있도록한다.
current_key = [False]*6

# 탐색 시작좌표 큐에 삽입, 마지막 매개변수는 다시 길을 되돌아갈수있는지에 대한정보
queue = deque()
queue.append([s, e, current_key, False])


# 네가지 방향에 대한 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    # visited배열을 만들어서 이동의 결과를 기록
    # 열쇠를 획득한 경우가 아니면 한번 왔던길로 되돌아가는 경우는 없도록 한다.
    # 열쇠를 획득하였다면 왔던길로 되돌아 갈수 있도록 한다.
    # 큐에 키 리스트를 함께 넘겨서 현재시점에서 획득한 키가 존재할경우에만 문을 발견했을때 넘어가도록 한다.
    # '1'의 좌표 x,y에 도달하면 탐색을 종료하고 visited[x][y]를 정답으로 출력한다.
    # 좌표에 도달하지 못한채 반복이 종료되면 -1를 리턴한다.
    visited = [[-1]*m for _ in range(n)]
    visited[s][e] = 0  # 시작 좌표 0으로 처리
    while queue:
        x, y, current_key, allow = queue.popleft()
        # 목적지에 도달하였다면 탐색 종료, 정답 리턴
        if graph[x][y] == '1':
            return visited[x][y]
        # 네 방향에 대해 탐색 수행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어나지 않으면서 방문하려는 좌표가 벽이 아닌경우에만
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
                # 만약 방문하려는 좌표가 '.'이라면
                if graph[nx][ny] == '.' or graph[nx][ny] == '1' or graph[nx][ny] == '0':
                    # 아직 방문하지 않은 좌표라면,
                    # 혹은 방문하였더라도 새로운 키를 획득하여 길을 되돌아갈 자격을 얻었다면
                    if visited[nx][ny] == -1 or allow:
                        visited[nx][ny] = visited[x][y] + 1  # 방문정보 갱신
                        # 키 정보와 함께 큐에 좌표 삽입
                        if allow:
                            queue.append([nx, ny, current_key, True])
                        else:
                            queue.append([nx, ny, current_key, False])
                # 방문하려는 좌표가 열쇠 혹은 문이라면
                else:
                    if visited[nx][ny] == -1:  # 이미 열쇠를 주운 경우는 방문x
                        # 열쇠인지 확인
                        if graph[nx][ny] in key:
                            # 열쇠를 만났다면 열쇠 리스트를 복사하고, 발견한 열쇠만 True처리
                            update_key = [False]*6
                            update_key[key[graph[nx][ny]]] = True
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append([nx, ny, update_key, True])
                        # 방문인지 확인
                        elif graph[nx][ny] in door:
                            # 해당 방문 열쇠를 보유중인지 확인
                            if current_key[door[graph[nx][ny]]]:
                                visited[nx][ny] = visited[x][y] + 1  # 방문처리
                                queue.append([nx, ny, current_key, False])

    # bfs종료전까지 목적지에 도달하지 못하였다면 -1을 출력한다.
    return -1


print(bfs())
