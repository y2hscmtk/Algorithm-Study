n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 사다리타기 구현
def play_game():
    destiny = [0]*(n+1) # 도착지 정보
    # 1번 플레이어(1번 열)부터 사다리 타기 수행
    # 현재 행에서 사다리가 존재한다면 열 변경 후 한 칸 내려가기
    # 현재 행에 사다리가 존재하지 않는다면 내려가기만 수행
    for player in range(1,n+1):
        col = player
        for row in range(1,16):
            # 왼쪽으로 가는 사다리가 존재하는지 확인
            if board[row][col-1] == True:
                col-=1 # 왼쪽 사다리로 이동
            # 오른쪽으로 가는 사다리가 존재하는지 확인
            elif board[row][col] == True: # 현재칸에 사다리 존재할 경
                col+=1 # 오른쪽 사다리로 이동
        destiny[player] = col # 도착 결과 기록
    return destiny

# 사다리 선택
def select_ladder(idx,cnt):
    global min_select_count
    # 가지치기 - 선택된 사다리의 개수가 이미 최소로 설정해둔 값을 넘어선다면 더 탐색할 필요 없음
    if min_select_count <= cnt:
        return
    # 현재 선택된 사다리정보로 게임 결과 확인 - 같을 경우 최소개수 갱신
    if play_game() == result:
        min_select_count = min(min_select_count,cnt)
    if idx == m: # m개 선택시 종료
        return
    # 사다리 선택
    for i in range(idx,m):
        a,b = edges[i]
        board[b][a] = True
        select_ladder(i+1,cnt+1)
        board[b][a] = False # 백트래킹

board = [[False]*(n+1) for _ in range(16)]

# 모든 사다리 선택 상태로 변경
for a,b in edges:
    board[b][a] = True
result = play_game() # 모든 사다리를 선택하였을때의 게임 결과 저장

# 모든 사다리 비선택 상태로 변경
board = [[False]*(n+1) for _ in range(16)]

min_select_count = 16
select_ladder(0,0)
print(min_select_count)