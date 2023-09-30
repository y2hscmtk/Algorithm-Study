# https://www.acmicpc.net/problem/1004
'''
이론 참조 : https://v3.leedo.me/devs/50
1. 시작점과 끝점이 모두 원 안에 있을때 => 카운팅x(궤도를 통과하지 않아도 목적지 도달 가능)
2. 시작점과 끝점 둘 중 하나가 원 밖에 있을때 => 카운팅(궤도를 통과해야 목적지 도달 가능)
3. 시작점과 끝점이 모두 원 밖에 있을때 => 카운팅x(궤도를 통과하지 않아도 목적지 도달 가능)
어떤점과 원의 중심 사이의 거리가 반지름보다 작다면 => 원 안에 있는것
'''
import math
for _ in range(int(input())):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())  # 시작점(x1,y1) 도착점(x2,y2)
    for _ in range(int(input())):  # 행성들 입력받기
        cx, cy, r = map(int, input().split())
        # 시작점이 해당 원 안에 있는지 확인
        isStartIn = False
        if math.sqrt((x1-cx)**2 + (y1-cy)**2) <= r:
            isStartIn = True
        # 끝점이 해당 원 안에 있는지 확인
        isOutIn = False
        if math.sqrt((x2-cx)**2 + (y2-cy)**2) <= r:
            isOutIn = True
        # 둘 중 하나가 원 밖에 존재한다면 => 카운팅 + 1
        if isStartIn ^ isOutIn:  # XOR연산을 통해, 두 값이 다른 경우(한 점이 원 안에 존재)확인
            result += 1
    print(result)
