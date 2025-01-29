'''
n x n 크기의 격자 칸
n개의 칸에 색칠, 각 행과 열에 정확히 1개의 색칠된 칸만 존재
색칠된 수들의 합의 최대값
'''
n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

max_sum = 0

visited = [False]*n # n개의 열에 대한 방문 정보
def select_num(row,curr_sum):
    global max_sum
    if row == n: # 마지막 행까지 다 도달한 경우 정답 갱신
        max_sum = max(max_sum, curr_sum)
        return
    
    # 현재 행을 기준으로 0열부터 n-1열까지 수 순차 선택
    for i in range(n):
        # 이전까지의 선택들에서 i번째 열을 선택하지 않은 경우
        if not visited[i]: 
            visited[i] = True
            select_num(row+1, curr_sum + grid[row][i])
            visited[i] = False

select_num(0,0)
print(max_sum)
    