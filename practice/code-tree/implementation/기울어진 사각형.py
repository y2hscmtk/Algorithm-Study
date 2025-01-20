'''
대각선 이동 원리 유형
대각선으로 이동하여 기울어진 직사각형을 이루며 이동하며 적힌 숫자들의 합이 최대가 되는 경우 반환
이동하는 도중 격자 밖으로 벗어나면 안된다.

1. 최대로 가능한 대각선의 길이 계산 - 최대 n까지 가능 - 가장 긴 대각선 (n*n)
2. 탐색 시작할 위치 정하기 (n*n)
3<=n<=20

O(n^4) = 400*400 = O(160000)

'''
n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

# 영역 검사
def in_range(x,y):
    return 0<=x<n and 0<=y<n


# 탐색
# 탐색 과정중 영역을 벗어나는 경우는 고려 x
def search(x,y):
    # 1번 경로로 이동시 - x-1,y+1 # 2번 경로로 이동시 - x-1,y-1
    # 3번 경로로 이동시 - x+1,y-1 # 4번 경로로 이동시 - x+1,y+1
    dxs = [-1,-1,1,1]; dys = [1,-1,-1,1]
    temp_max_sum = 0
    for px in range(1,n+1):
        for py in range(1,n+1):
            c_x,c_y = x,y
            fail = False
            temp_sum = 0
            # 이동할 방향 설정
            for dx,dy in zip(dxs,dys):
                if fail: # 설정한 크기만큼 이동하는것이 실패한 경우
                    break
                if (dx,dy) == (-1,1) or (dx,dy) == (1,-1):
                    for _ in range(px):
                        nx,ny = c_x + dx, c_y + dy
                        if not in_range(nx,ny):
                            fail = True
                            break
                        temp_sum += grid[nx][ny]
                        c_x,c_y = nx,ny
                else:
                    for _ in range(py):
                        nx,ny = c_x + dx, c_y + dy
                        if not in_range(nx,ny):
                            fail = True
                            break
                        temp_sum += grid[nx][ny]
                        c_x,c_y = nx,ny
            # 실패하지 않았다면
            if not fail:
                temp_max_sum = max(temp_max_sum, temp_sum)
    return temp_max_sum                

max_sum = 0 # 최대 숫자들의 합
# 탐색 시작 위치 지정
for i in range(n):
    for j in range(n):
        max_sum = max(max_sum, search(i,j))
                
print(max_sum)
