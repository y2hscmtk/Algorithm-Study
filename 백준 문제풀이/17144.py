# https://www.acmicpc.net/problem/17144
# 아래 과정을 T번 반복
# 1. 미세먼지 확산 => 현재 칸//5, 범위를 벗어나지 않고, 기계가 없는 공간이 아니면 상하좌우 이동,
# 1.1. 미세먼지 현황 업데이트 => 현재 칸 - 이동횟수*확산량
# 2. 공기청정기 작동 => 반시계 이동, 시계 이동 구현 => x1,x2,y1,y2 값 입력받아서 시계방향,반시계방향으로 회전하는 함수 작성
# 3. T초 후, 남아있는 미세먼지 총합 출력 => 총합 계산하는 함수 작성
R,C,T = map(int,input().split())
dust = [list(map(int,input().split())) for _ in range(R)]


# 현재 남아있는 미세먼지 총합 출력
def curr_dust():
    s = 0
    for i in range(R):
        for j in range(C):
            if dust[i][j] != -1:
                s+=dust[i][j]
    return s


while T != 0:
    T-=1 # 1초 경과
    # 미세먼지 확산

    # 확산 후 업데이트

    # 공기 청정기 작동
    # 1. 반시계 작동(위쪽)
    
    # 2. 시계 작동(아래쪽)  

print(curr_dust())