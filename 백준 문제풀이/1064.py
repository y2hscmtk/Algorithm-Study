# https://www.acmicpc.net/problem/1064
'''
1. D를 꼭 찾을 필요가 없다. => 세 점으로 인해 길이를 구할 수 있으므로
<가능한 경우의 수> CA-AB / AC-CB / AB-BC
                         D
                       - 
                     -
    A-----B        A     B      A-----B
    |              |   -             - 
    |              | -              -
    C     D        C         D     C

2. 평행사변형을 만들 수 없는 경우 => 세 점이 모두 한 점에 있는 경우(기울기로 확인)
'''
import sys
import math
xA, yA, xB, yB, xC, yC = map(int, input().split())
# 평행사변형을 만들 수 없는 지 확인(세 점이 모두 한 점에 있는지 확인)
# if ((xB-xA)/(yB-yA)) == ((xC-xB)/(yC-yB)): => 0으로 나눌 수 없음
if ((xB-xA)*(yC-yB)) == ((yB-yA)*(xC-xB)):
    print(-1.0)
else:  # 평행 사변형을 만들 수 있다면
    # 만들 수 있는 사각형의 둘레 계산
    # (AC+AB)*2 혹은 (AC+BC)*2 혹은 (AB+BC)*2
    AB = math.sqrt((xB-xA)**2 + (yB-yA)**2)
    AC = math.sqrt((xC-xA)**2 + (yC-yA)**2)
    BC = math.sqrt((xC-xB)**2 + (yC-yB)**2)
    parallelogram = [(AC+AB)*2, (AC+BC)*2, (AB+BC)*2]
    print(max(parallelogram)-min(parallelogram))
