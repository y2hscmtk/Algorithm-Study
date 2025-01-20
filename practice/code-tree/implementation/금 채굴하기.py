'''
마름모의 '중간 지점'을 정해야 쉽게 풀 수 있다.
마름모의 정의를 이용하여 
전체 영역에서 현재 중심으로 삼은 지역 사이의 거리가 마름모의 k범위보다 작거나 같다면 마름모 안의 숫자가 된다.

'규칙' 과 '정의'를 생각하면서 어떻게 풀지 설계하자

K는 어림잡아 2*N 이상볼 필요가 없다 -> 2N 이상만 되어도, 모든 영역을 다 검사할 수 있음
'''

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

# 마름모의 중심 지역을 설정하였을 때 영역 내의 금 개수 반환
def find_gold(x,y):
    count = 0
    for i in range(n):
        for j in range(n):
            # (i,j)와 (x,y)사이의 멘헤튼 거리가 k이하라면 해당 좌표는 마름모 내부 좌표
            if abs(i-x) + abs(j-y) <= k:
                if grid[i][j] == 1: # 금이 있는 지역이라면
                    count += 1
    
    return count


k = 0
max_count = 0 # 최대로 탐색 가능한 금의 수 
while True:
    if k == 2*n: # 충분한 영역을 탐색하였다면 종료
        break
    
    # 마름모의 중심이 될 수 있는 영역 설정
    cost = k*k + (k+1)*(k+1) # 현재 시점에서의 공사 비용
    for i in range(n):
        for j in range(n):
            count = find_gold(i,j)
            price = count*m
            # 현재 이득이 공사 비용보다 많거나 같다면 - 손해가 없다면
            if cost <= price:
                max_count = max(max_count, count) # 채굴한 금의 수 갱신

    k+=1 # K값 증가

print(max_count) # 최대로 채굴한 금의 수 출력