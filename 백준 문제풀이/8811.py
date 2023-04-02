# https://www.acmicpc.net/problem/8911
'''
F: 한 눈금 앞으로
B: 한 눈금 뒤로
L: 왼쪽으로 90도 회전
R: 오른쪽으로 90도 회전

거북이가 지나간 모든 경로를 포함하는 가장 작은 직사각형의 넓이를 구해라
같은 선으로만 이동한 경우는 선분이 된다. 선분의 경우 넓이는 0이다.
'''
import sys
# 북 동 남 서
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
# 북 동 남 서
d = [0, 1, 2, 3]
# + dx[0] + dy[0] => 북쪽방향일때 F명령(위로 한칸)
# - dx[0] - dy[0]=> 북쪽방향일때 B명령(아래로 한칸)
# + dx[1] + dy[1] => 남쪽방향일때 F명령(아래로 한칸)
# - dx[1] - dy[1]=> 남쪽방향일때 B명령(위로 한칸)
# + dx[2] + dy[2]=> 동쪽방향일때 F명령(오른쪽으로 한칸)
# - dx[2] - dy[2] => 동쪽방향일때 B명령(왼쪽으로 한칸)
# + dx[3] + dy[3]=> 서쪽방향일때 F명령(왼쪽으로 한칸)
# - dx[3] - dy[3]=> 서쪽방향일때 F명령(오른쪽으로 한칸)

# 거북이가 이동한 경로를 배열에 담고
# 배열의 x값중 가장 작은값과 큰값을 빼서 한 변으로 삼고
# 배열의 y값중 가장 작은값과 큰값을 빼서 한 변으로 삼아서 곱한 값을 출력한다.

t = int(input())
for _ in range(t):
    commands = input()
    # 명령에 맞춰서 동작 수행
    turtle = [[0, 0]]  # 거북이는 처음에 0,0에 있고
    direction = 0  # 북쪽을 바라보고 있다.
    x, y = 0, 0  # 거북이의 현재 위치
    for command in commands:
        # 앞으로 한칸 명령
        if command == 'F':
            x += dx[direction]
            y += dy[direction]
            turtle.append([x, y])  # 거북이 이동경로 삽입
        # 한칸 뒤로 명령
        elif command == 'B':
            x -= dx[direction]
            y -= dy[direction]
            turtle.append([x, y])  # 거북이 이동경로 삽입
        # 왼쪽으로 90도 회전명령
        elif command == 'L':
            direction = d[direction-1]  # 방향 바꾸기
        # 오른쪽으로 90도 회전명령
        elif command == 'R':
            if direction+1 > 3:
                direction = d[0]
            else:
                direction = d[direction+1]  # 방향 바꾸기

    min_x, min_y = 0, 0
    max_x, max_y = 0, 0
    for t_x, t_y in turtle:
        if t_x > max_x:
            max_x = t_x
        if t_y > max_y:
            max_y = t_y
        if t_x < min_x:
            min_x = t_x
        if t_y < min_y:
            min_y = t_y

    # 최소 직사각형 구하기
    print(abs(max_x-min_x)*abs(max_y-min_y))
