# https://www.acmicpc.net/problem/14620
'''
# 1. 꽃을 심을 자리를 선택 - 3개 골라야함
# 2. 꽃이 죽는지 사는지 확인 - 함수 작성
# 3. 꽃을 심을 장소의 가격이 최소가 되어야 한다.
'''
n = int(input())
cost = [list(map(int,input().split())) for _ in range(n)]

# 해당 좌표내의 꽃이 존재하는지 여부 파악
flower = [[False]*n for _ in range(n)]

# 꽃이 자랄수있는 조건을 만족하는 영역
area = []
for i in range(1,n-1):
    for j in range(1,n-1):
        area.append((i,j))

# 현재 선택한 지역에 꽃을 심을 경우 소비되는 가격
def get_cost():
    temp_cost = 0
    for i in range(n):
        for j in range(n):
            if flower[i][j]:
                temp_cost += cost[i][j]
    return temp_cost

def is_success():    
    global flower
    dxs = [0,0,-1,1]; dys = [-1,1,0,0]
    flower = [[False]*n for _ in range(n)]
    for x,y in selected_area:
        if flower[x][y]: # 이미 꽃이 존재한다면
            return False # 실패
        flower[x][y] = True # 꽃을 피우고
        # 상하좌우 인접한 장소에 꽃을 피운다.
        for dx,dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy
            # 이미 꽃이 존재하는 땅이라면 꽃을 심을 수 없음
            if flower[nx][ny]:
                return False
            flower[nx][ny] = True # 꽃 심기
    return True

selected_area = [ ] # 꽃을 심기 위해 선택된 지역
min_cost = float('inf')
def select_area(start, cnt):
    global min_cost
    if cnt == 3: # 꽃을 심을 장소를 모두 골랐다.
        # 꽃이 모두 생존하는지 확인
        if is_success():
            # 그로인한 비용이 최소가 되는지 확인
            min_cost = min(min_cost, get_cost())
        return
    
    for i in range(start, len(area)):
        selected_area.append(area[i])
        select_area(i+1, cnt+1)
        selected_area.pop()

select_area(0,0)
print(min_cost)