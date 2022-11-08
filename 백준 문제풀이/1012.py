# https://www.acmicpc.net/problem/1012

'''
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 
0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1

'''

'''
아이디어1
서로 인접한 그룹의 개수가 몇개인지 그래프 탐색을 통해 파악하면 된다.
'''


from collections import deque
t = int(input())


def append_queue(queue, start, end):  # 인접한 정점들을 큐에 삽입하는 연산
    queue.append([start+1, end])
    queue.append([start, end+1])
    queue.append([start-1, end])
    queue.append([start, end-1])


def bfs(data, start, end):
    global m, n
    data[start][end] = 0  # 방문처리
    queue = deque()
    append_queue(queue, start, end)
    while queue:
        node = queue.popleft()
        s = node[0]
        e = node[1]
        if 0 <= s < n and 0 <= e < m:
            if data[s][e] == 1:
                data[s][e] = 0  # 방문처리
                append_queue(queue, s, e)  # 인접 정점 삽입


m, n, k = 0, 0, 0

for _ in range(t):
    # 가로길이M(1 ≤ M ≤ 50), 세로길이 N(1 ≤ N ≤ 50), 배추개수 K(1 ≤ K ≤ 2500)
    group = 0
    m, n, k = map(int, input().split())
    data = []
    for i in range(n):
        data.append([])
        data[i] = list(0 for _ in range(m))
    for _ in range(k):  # 배추 삽입 연산
        x, y = map(int, input().split())
        data[y][x] = 1  # 배추가 있다는 의미
    # 여기서부터 그룹 검사 => 정점들을 하나씩 뽑아가며 검사
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                group += 1  # 새로운 그룹을 발견했다는 의미
                bfs(data, i, j)
    print(group)
