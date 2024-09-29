# https://www.acmicpc.net/problem/13268
'''
시작점에서부터 5m의 간격을 두고 콘을 세워둠
0m    5m     10m     15m     20m
----- 1 ----- 2 ----- 3 ----- 4

한 세트는 아래와 같음
# 구간[0] 0 -> 5 -> 0 총 이동거리 10
# 구간[1] 0 -> 10 -> 0 총 누적 이동거리 10 + 20 = 30
# 구간[2] 0 -> 15 -> 0 총 누적 이동거리 10 + 20 + 30 = 60
# 구간[3] 0 -> 20 -> 0 총 누적 이동거리 10 + 20 + 30 + 40 = 100
한 세트의 총 이동 거리 100

예상 알고리즘
=> 그리디, 수학

예상 풀이방법
1. 현재 남아있는 이동가능 거리로 몇세트를 수행가능한지 확인 -> 100으로 나눔
2. 남아있는 이동가능 거리가 
    10미만 : 가능 구간 0~1
    10~30미만 : 가능 구간 0~2, 
    30이상~60미만 : 가능 구간 0~3
    60이상 : 가능 구간 0~4 
'''
move_able = int(input())

move_able = move_able%100 # 나머지 확인

# 시작점에 위치하는지 확인
if move_able == 0 or move_able == 10 or move_able == 30 or move_able == 60:
    print(0)
elif (0 < move_able < 10) or (10 <move_able<= 15) or (25 <= move_able < 30) or (30 < move_able <= 35) or (55 <= move_able < 60) or (60 < move_able <= 65) or (95 <= move_able < 100):
    print(1)
elif (15 < move_able < 25) or (35 < move_able <= 40) or (50 <= move_able < 55) or (65 < move_able <= 70) or (90 <= move_able < 95):
    print(2)
elif (40 < move_able < 50) or (70 < move_able <= 75) or (85 <= move_able < 90):
	print(3)
else:
	print(4)
