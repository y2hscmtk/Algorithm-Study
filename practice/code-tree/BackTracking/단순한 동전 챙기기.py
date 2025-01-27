'''
풀이 참조
R개의 동전 중 M(=3)개의 동전을 뽑는 모든 조합 생성
이후, 각 조합에 대해 이동거리를 계산하여 가능한 이동거리 중 최소값 구하기
'''
COIN_NUM = 9
INT_MAX = float('inf')

n = int(input())
m = 3 # 최소 3개 이상 골라야 함

grid = [input() for _ in range(n)]

coin_pos = [] # 각 동전이 현재 어디에 위치해 있는지 기록
selected_pos = [] # 선택된 좌표들

start_pos = (-1,-1)
end_pos = (-1,-1)

# 시작지점 도착지점 구하기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_pos = (i,j)
        if grid[i][j] == 'E':
            end_pos = (i,j)

# 각 동전의 위치 기록 - 증가하는 순대로 방문하기 위해 오름차순으로 위치 기록
for num in range(1, COIN_NUM + 1):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str(num):
                coin_pos.append((i,j))

ans = INT_MAX

# 두 점 a,b 사이의 멘헤튼 거리 계산
def dist(a,b):
    (ax,ay), (bx,by) = a, b
    return abs(ax - bx) + abs(ay - by)

# 현재 선택한 좌표들을 기준으로 이동한 총 이동거리 반환
def calc():
    # 시작 지점에서 처음 선택한 좌표까지의 거리 계산
    num_moves = dist(start_pos, selected_pos[0])
    for i in range(m-1): 
        num_moves += dist(selected_pos[i], selected_pos[i+1])
    num_moves += dist(selected_pos[m-1], end_pos)

    return num_moves

def find_min_moves(curr_idx, cnt):
    global ans

    if cnt == m: # 동전 3개 선택시
        ans = min(ans, calc())
        return
    
    # 모든 동전 선택시 종료
    if curr_idx == len(coin_pos):
        return

    # 동전을 선택하지 않는 경우
    find_min_moves(curr_idx + 1, cnt)
    
    # 동전을 선택하는 경우
    selected_pos.append(coin_pos[curr_idx])
    find_min_moves(curr_idx+1, cnt + 1)
    selected_pos.pop()

find_min_moves(0,0)

if ans == INT_MAX:
    ans = -1

print(ans)
