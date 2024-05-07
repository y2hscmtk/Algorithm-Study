# https://www.acmicpc.net/problem/20055
N,K = map(int,input().split())
# 해당 칸의 컨베이어 밸트의 내구도(길이 : 2N)
durability = list(map(int,input().split())) 
isRobot = [False]*(N) # 해당 칸에 로봇이 올라와있는지 아닌지

# 1. 벨트가 각 칸 위에 있는 로봇과 '함께' 한 칸 회전한다.
# => 단순히 '회전' 하는 것이므로 내구도 손실은 없다.
def rotateConveyor():
    global durability, isRobot
    last_dur = durability[-1]
    durability = [last_dur] + durability[:-1]
    last_robot = isRobot[-1]
    isRobot = [last_robot] + isRobot[:-1]
    # '내리는 칸'에 도달하게 되면 로봇은 내린다.
    if isRobot[-1]:
        isRobot[-1] = False

# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
# 만약 이동할 수 없다면 가만히 있는다.
# 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
def moveRobot():
    # 가장 먼저 벨트에 올라간 로봇부터 움직인다. => 배열의 뒤에서부터 움직인다.
    for i in range(N-2,-1,-1): # N-1번째에 도달하게 되면 로봇은 바로 내리므로
        if isRobot[i]: # 로봇이 있다면
            # 1. 이동하려는 칸에 로봇이 없어야 한다.
            # 2. 이동하려는 칸에 내구도가 1 이상 남아 있어야 한다.
            if not isRobot[i+1] and durability[i+1] > 0:
                isRobot[i],isRobot[i+1] = False, True # 로봇 이동
                durability[i+1] -= 1 # 로봇이 이동하였으므로 내구도가 1 감소한다.
                if i+1 == N-1: # 로봇이 '내리는 위치'에 도달하였다면 그 즉시 내린다.
                    isRobot[i+1] = False # 내린다.


# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
def putRobot():
    global isRobot, durability
    # 컨베이어 벨트의 0번째 인덱스에 로봇을 올린다.
    # 현재 0번째 칸의 내구도가 0이 아니라면 로봇을 올리 수 있다.
    if durability[0] != 0:
        isRobot[0] = True
        durability[0] -= 1 # 로봇이 올라갔으므로 내구도 1감소


# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
def checkStop(): # 멈춰야 하는지 확인한다.
    count = 0
    for d in durability:
        if d == 0:
            count+=1
            if count >= K:
                return True
    return False

step = 0
while True:
    step += 1
    rotateConveyor()
    moveRobot()
    putRobot()
    if checkStop():
        print(step) # 몇 번째 단계였는지 출력한다.
        break