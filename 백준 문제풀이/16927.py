# https://www.acmicpc.net/problem/16927
'''
1. 반시계 방향 회전 알고리즘 구현
2. 몇번의 '반시계 방향 회전'을 하면 초기 위치로 되돌아 오는지 계산하여 모듈러 연산(1 ≤ R ≤ 10^9 이므로)
3. N,M 두 값 중 하나는 짝수 => 테두리부터 2씩 깎아가면서 회전하면됨(속으로 파고 들어감2가 될 때 까지)
'''
import sys
input = sys.stdin.readline
N,M,R = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

def turn(s, e, cycle):
    global data
    if cycle <= 0:  # 회전할 필요가 없는 경우 바로 반환
        return
    
    rotation_count = R % cycle  # 실제 회전 횟수 계산
    for _ in range(rotation_count):
        temp = data[s][e]
        # 위쪽
        for y in range(e, M-e-1):
            data[s][y] = data[s][y+1]
        # 오른쪽
        for x in range(s, N-s-1):
            data[x][M-e-1] = data[x+1][M-e-1]
        # 아래쪽
        for y in range(M-e-1, e, -1):
            data[N-s-1][y] = data[N-s-1][y-1]
        # 왼쪽
        for x in range(N-s-1, s, -1):
            data[x][e] = data[x-1][e]
        data[s+1][e] = temp

# 두번째 사이클 => 높이 2감소, 가로 2감소
# 2*(N-3) + 2*(M-3) => 2(N+M)-12 => 8씩 차이남
cycle = 2*(N-2)+2*(M-2)
s = 0
while s < N // 2:  # 속으로 파고들면서 각 테두리를 회전
    turn(s, s, cycle)
    cycle -= 8
    s += 1

for d in data:
    print(*d)
