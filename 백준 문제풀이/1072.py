# https://www.acmicpc.net/problem/1072
'''
게임 기록은 다음과 같이 생겼다.
게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.
'''
'''
이분탐색
mid에서 승률이 변화하였다면, 더 낮은 횟수로도 승률이 변했는지 탐색해야하므로
high를 mid로 바꾸어 다시 탐색을 진행한다.
mid에서 승률이 변화하지 않았다면, 더 많은 게임을 해야한다는 것을 의미하므로
low를 mid+1로 바꾸어 다시 탐색을 진행한다.
'''