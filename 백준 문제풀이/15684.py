# https://www.acmicpc.net/problem/15684
'''
N개의 세로선과 M개의 가로선으로 이루어진 사다리 => N * M 형태의 배열로 구성
사다리게임의 특성상 아래로 내려가는 것은 자유롭고, 내려가는 도중에 가로길을 만나면 가로로 이동하게 된다.
각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H개로 정해져있다.

사다리 게임은 각각의 세로선마다 게임을 진행하고, 세로선의 가장 위에서부터 아래 방향으로 내려가야 한다.
가로선을 만나면 가로선을 이용해 옆 세로선으로 이동한 다음, 이동한 세로선에서 아래 방향으로 이동해야 한다.

사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다. 이때, i번 세로선의 결과가 i번이 나와야 한다.
그렇게 하기 위해서 추가해야 하는 가로선 개수의 최솟값을 구하는 프로그램을 작성하시오.

i번 세로선의 결과가 i번이 나오도록 사다리 게임을 조작하려면, 추가해야 하는 가로선 개수의 최솟값을 출력한다.
만약, 정답이 3보다 큰 값이면 -1을 출력한다. 또, 불가능한 경우에도 -1을 출력한다.
'''
N,M,H = map(int,input().split()) # 세로선의 개수(열의 개수), 가로선의 개수(행의 개수), 세로선마다 놓을 수 있는 위치의 개수 H

# 가장 위에 있는 점선의 번호는 1번, 아래로 내려갈 때마다 1이 증가
# 세로선은 가장 왼쪽에 있는 것의 번호가 1번, 오른쪽으로 갈 때마다 1이 증가한다.
ladder = [[False]*(N+2) for _ in range(H+1)] # 편의를 위해 0번째 인덱스로 패딩

# 1. 사다리 놓기
for _ in range(M): # 가로선의 정보
    a,b = map(int,input().split()) # b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미 
    # => a는 행의 인덱스, b는 열의 인덱스
    ladder[a][b] = True
    
# 2. 후보 선택(사다리를 놓을 수 있는)
# 조건 : 사다리는 가로로 연속해서 놓을 수 없음
position = []
for i in range(1,H+1): 
    for j in range(1,N+1): # 마지막 사다리 고려 x(어차피 오른쪽 사다리 못놓음)
        # 현재 위치에 사다리가 없어야 한다.
        if not ladder[i][j]:
            position.append((i,j))

# 3. positon에서 0~3개 뽑기
def select_position(start,select):
    global ladder,find
    # count개 골랐다면
    if select==count:
        # 성공조건을 만족하는지 확인
        if success():
            find = True # 찾았음
        return

    for i in range(start,len(position)):
        x,y = position[i]
        # 선택 가능하다면
        if not ladder[x][y-1] and not ladder[x][y+1]:
            ladder[x][y] = True # 사다리 놓기
            select_position(i+1,select+1) # 사다리 한개 선택
            ladder[x][y] = False # 백트래킹

# 최종 조건 확인용
def success():
    for i in range(1,N+1): 
        start,curr = i,i # 시작 위치 저장
        # i번 세로선의 결과가 i번이 나오는지 확인
        for j in range(1,H+1): # 가로선을 의미 => j값이 증가함에따라 아래로 이동한다.
            if ladder[j][curr] == True: # 오른쪽으로 이동이 가능하다면
                curr+=1
            elif ladder[j][curr-1] == True: # 왼쪽으로 이동 가능한지 확인
                curr-=1 # 왼쪽으로 이동
        # 끝에 도달하였을때 start와 같은지 확인
        if curr != start: # 하나라도 같지 않다면
            return False
    return True # 무사히 통과했다는 것은 i번째가 모두 i번째에 도달하였다는 것을 의미

for count in range(4): # 0~3개까지 고를 수 있음
    find = False
    select_position(0,0) # 사다리 고르기
    if find: # 찾으면 종료
        result = count
        break
else:
    result = -1
print(result)