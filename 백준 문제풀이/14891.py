# https://www.acmicpc.net/problem/14891
'''
1.
회전연산을 수행하기전, 각각 어느방향으로 회전을 할것인지 반복문을 통해 톱니바퀴의 양극 확인
회전이 항상 첫번째 바퀴에서부터 시작하지 않음(양끝의 톱니바퀴를 모두 비교해야함)

다음 톱니바퀴의 회전에 영향을 주는 인덱스
현재 톱니바퀴의 오른쪽(2) - 다음 톱니바퀴의 왼쪽(6) 

같은 극을 가리키고 있다면, 그 다음 톱니바퀴들도 회전하지 않으므로 반복문 종료
다른 극을 가리키고 있다면, 해당 톱니바퀴는 이전 톱니바퀴의 방향과 반대로(*-1) 회전할것이고 그 다음 톱니바퀴도 회전 할 가능성 존재

2.
방향이 결정된 이후, 각 톱니바퀴의 방향 바꾸기 연산 수행
왼쪽으로 한칸씩 당기기(-1), 오른쪽으로 한칸씩 밀기(1)
'''
from collections import deque
# 4개의 톱니바퀴의 현재 상황 입력받기
gears = []
# 4개의 톱니바퀴 상태를 입력받아서 리스트에 추가
for _ in range(4):
    gear_state = input()
    gear_state_list = [int(bit) for bit in gear_state]  # 이진수 문자열을 정수 리스트로 변환
    gears.append(gear_state_list)


# n : 회전시킬 톱니바퀴
# d : 방향
def check_direction(n):
    '''
    현재 톱니바퀴의 오른쪽(2) - 다음 톱니바퀴의 왼쪽(6) 
    '''
    global direction
    dx = [1, -1]
    queue = deque()
    queue.append(n)
    # 양 톱니바퀴가 회전할 것인지 확인
    # 좌,우 인덱스로의 톱니바퀴 확인(영역 벗어나면 해당 방향으로의 탑색 종료)
    while queue:
        x = queue.popleft()
        for i in range(len(dx)):
            next_gear = x + dx[i]
            # 0,1,2,3번 톱니바퀴인 경우에만 확인
            # next_gear는 넘어온 톱니바퀴
            if 0 <= next_gear < 4:
                # 이미 방향이 정의되어 있다면 방문한 톱니바퀴나 마찬가지이므로 넘어가기
                if direction[next_gear] != 0:
                    continue
                if i == 0:  # i가 0 => 오른쪽 톱니바퀴를 비교하고 싶음
                    l, r = 2, 6  # (n번 톱니바퀴의 오른쪽(2)과 오른쪽 톱니바퀴의 왼쪽(6)을 확인)
                else:  # i가 1 => 왼쪽 톱니바퀴를 비교하고 싶음
                    l, r = 6, 2  # (n번 톱니바퀴의 왼쪽(6)과 오른쪽 톱니바퀴의 오른쪽(2)을 확인)
                if gears[x][l] != gears[next_gear][r]:  # 같지 않다면
                    direction[next_gear] = direction[x]*(-1)  # 반대방향으로 회전시켜야함
                    # 회전에 영향을 받은 톱니바퀴라면, next_gear와 연결된 톱니바퀴들도 비교해야함
                    queue.append(next_gear)


# 톱니바퀴 실제로 회전
def rotate_gear():
    global gears

    # 각 톱니바퀴의 방향을 확인
    for i in range(len(direction)):
        if direction[i] == 0:  # 회전하지 않는경우 넘어가기
            continue
        # 회전할 경우
        # 오른쪽 회전(시계방향)
        if direction[i] == 1:
            temp = gears[i][-1]
            for j in range(len(gears[i])-1, 0, -1):
                gears[i][j] = gears[i][j-1]
            gears[i][0] = temp
        else:
            temp = gears[i][0]
            for j in range(len(gears[i])-1):
                gears[i][j] = gears[i][j+1]
            gears[i][-1] = temp


# 최종 톱니바퀴에 대한 점수 계산
def calc_point():
    point = 0
    '''
    <점수 계산>
    12시 방향은 0번 인덱스의 값
    1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
    2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
    3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
    4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
    N극은 0, S극은 1
    '''
    # N극(0)은 어차피 0점이니까 S극인지만 확인
    if gears[0][0] == 1:
        point += 1
    if gears[1][0] == 1:
        point += 2
    if gears[2][0] == 1:
        point += 4
    if gears[3][0] == 1:
        point += 8
    return point


# 회전 연산 수행(몇번 톱니바퀴를, 어떤 방향으로 회전시킬 것인지 왼쪽(-1) 오른쪽(1))
for _ in range(int(input())):
    # 각각의 톱니바퀴를 어느방향으로 회전시킬 것인지
    direction = [0, 0, 0, 0]  # 현재 연산에서의 회전방향 초기화
    # 회전시킬 톱니바퀴의 번호, 회전시킬 방향
    n, d = map(int, input().split())
    direction[n-1] = d  # 톱니바퀴 방향 입력
    # 각각의 톱니바퀴가 어느방향으로 회전해야 하는지 확인
    check_direction(n-1)  # 계산을 용이하게 하기 위해 -1
    # 톱니바퀴를 실제로 회전
    rotate_gear()

# 최종 연산 이후, 포인트를 얼마나 보유하고 있는지 출력
print(calc_point())
