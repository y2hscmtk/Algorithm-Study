# https://www.acmicpc.net/problem/17135
'''
<예상>
구현,시뮬레이션,브루트포스,백트래킹
'''
n,m,d = map(int,input().split()) # d는 궁수의 공격제한 거리
game = [list(map(int,input().split())) for _ in range(n)]
x = n # 궁수는 가장 아래쪽에 있으므로 x좌표는 고정됨
result = 0 # 공격 가능한 최대 적의 수
position = [] # 궁수 위치
copy_game = [] # 게임판 복사용

# 1. 궁수 3명을 배치한다.
def collocate_archer(start):
    # 2. 배치가 끝나면 게임 시작
    if len(position) == 3: # 3명 배치 완료시 게임 시작
        game_start()
    for i in range(start,m):
        position.append(i)
        collocate_archer(i+1)
        position.pop()

# 적이 남아있는지 검사
def no_enemy():
    for i in range(n):
        for j in range(m):
            if copy_game[i][j] == 1:
                return False # 적이 남아있다면
    return True # 남아있는 적이 없음

# 공격 알고리즘에 따라 궁수 공격 시작
def defense():
    global copy_game
    # (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다.
    # 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 
    # 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다.
    # 조건을 만족하는 적들 임시 배열에 담아두기
    # 같은 적을 동시에 공격하는 경우가 있을 수 있다.
    # 공격당하는 적에게 표식(2)을 남기고 한번에 제거 후 카운팅
    for p in range(3):
        r,c = x, position[p] # 궁수의 좌표 r,c
        enemy = [] # 적들의 위치를 담을 배열
        for i in range(n-1,-1,-1):
            for j in range(m):
                if copy_game[i][j] != 0: # 적을 발견하였다면(1또는 2 같은 타겟을 설정할 수 있음)
                    distance = abs(r-i) + abs(c-j)
                    if distance <= d: # 거리 조건 확인
                        enemy.append([abs(r-i) + abs(c-j),i,j])
        if len(enemy) != 0: # 해당 궁수가 죽일 수 있는 적이 없을 수 있음
            enemy.sort(key=lambda x:(x[0],x[2])) # 오름차순 정렬후 가장 앞 값을 죽일 타겟으로 선정
            r2 = enemy[0][1]; c2 = enemy[0][2]
            copy_game[r2][c2] = 2 # 표식 남기기
    count = 0 # 몇명의 적을 죽였는지
    for i in range(n):
        for j in range(m):
            if copy_game[i][j] == 2: # 표식이 남겨져있다면
                count+=1 # 죽은것이므로 카운트
                copy_game[i][j] = 0 # 제거 처리
    return count

# 적 이동
def enemy_move():
    global copy_game
    # 편의를 위해 가장 아래줄은 따로
    for j in range(m):
        if copy_game[n-1][j] == 1:
            # 성에 닿으면 사라진다.
            copy_game[n-1][j] = 0 # 적이 성에 닿은 판정
        copy_game[n-1][j] = copy_game[n-2][j]

    # 밑에서 2번째 줄부터 1칸씩 이동
    for i in range(n-2,0,-1):
        for j in range(m):
            copy_game[i][j] = copy_game[i-1][j]
            
    # 가장 윗 칸은 전부 0으로 처리
    for j in range(m):
        copy_game[0][j] = 0

# 현재 궁수의 배치로 몇명의 적을 잡을 수 있는지 시뮬레이션
def game_start():
    global copy_game,result
    temp = 0 # 총 몇명의 적을 죽일 수 있는지
    copy_game = [g[:] for g in game]
    while True:
        # 모든 적이 격자판에서 제외되면 게임이 끝난다.
        if no_enemy():
            break
        # 궁수의 공격이 끝나면, 적이 이동한다.
        # 궁수가 먼저 공격
        temp += defense() # 궁수 공격 => 몇명 죽였는지 확인
        # 적 이동
        enemy_move() # 한칸씩 아래로 이동, 성이 있는곳에 도달하였다면 제거된다.
    result = max(result,temp) # 정답 갱신

# 궁수 배치 후 게임 시작
collocate_archer(0)
# position = [0,2,4]
# game_start()
print(result)