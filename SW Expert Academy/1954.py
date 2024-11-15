# 방향 벡터 정의
# 오른쪽, 아래, 왼쪽, 위
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def print_snail(t,n):
    print(f'#{t}')
    graph = [[0 for _ in range(n)] for _ in range(n)]
    d = 0 # 시작 방향 : 오른쪽
    x,y = 0,0 # 시작 위치
    graph[x][y] = 1
    num = 2 # 기록 시작 숫자
    bound_min,bound_max = 0,n
    while True:
        if graph[x][y] == 0:
            graph[x][y] = num
            num += 1
        
        # 경계 넘어설 경우 방향 회전 필요
        nx = x + dx[d]; ny = y + dy[d]
        if ny == bound_max or ny < bound_min or nx == bound_max or nx < bound_min:
            d = (d+1) # 방향 변경
            if d == 4: # 안쪽으로 들어가야 하는 경우
                d = 0; bound_min+=1; bound_max-=1
                x+=1; y+=1
                if bound_min > bound_max:
                    break
            continue
        x = nx; y = ny
    
    # 완성된 결과물 출력    
    for g in graph:
        print(*g)

for i in range(int(input())):
    n = int(input())
    print_snail(i+1,n)