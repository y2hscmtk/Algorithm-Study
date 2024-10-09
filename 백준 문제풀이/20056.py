# https://www.acmicpc.net/problem/20056
'''
i번째 파이어볼의 위치는 r,c 질량은 m, 방향은 d, 속력은 s,
각 행과 열은 1에서부터 시작 -> r,c -=1 필요
    
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.
'''
import sys
# N x N 크기의 격자, M 파이어볼의 개수, K 수행할 명령의 수
N,M,K = map(int,input().split())
fire_balls = []
# M개의 파이어볼에 대한 정보 입력받기
for _ in range(M):
    # r,c,m,d,s 좌표,질량,방향,속력
    r,c,m,d,s = list(map(int,input().split()))
    fire_balls.append((r-1,c-1,m,d,s))
# 방향 d
'''
7	0	1
6	 	2
5	4	3
'''
dx = [-1,-1,0,1,1,1,0,-1]; dy = [0,1,1,1,0,-1,-1,-1]

def move():
    global fire_balls
    temp_fire_balls = [] # 분할된 파이어볼 저장용
    dict = {} # 파이어볼 위치별 저장용
    # 좌표 -1 필요
    for r,c,m,d,s in fire_balls:
        # 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
        # - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
        # 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다. -> 모듈러 연산 필요
        nx = (r + s*dx[d]); ny = (c + s*dy[d])%N
        if nx<0:
            nx = (nx + N)%N
        elif ny < 0:
            ny = (ny + N)%N
        elif nx > N:
            nx = nx % N
        elif ny > N:
            ny = ny % N
        key = f'{nx},{ny}'
        if key not in dict:
            dict[key] = [(nx,ny,m,d,s)]
        else:
            dict[key].append((nx,ny,m,d,s))
    # 이동이 끝난 뒤 2개 이상의 파이어볼이 있는 칸에서는 아래와 같은 일이 이뤄진다.
    for key in dict:
        # 1개 이하인 경우는 파이어볼 배열에 삽입
        if len(dict[key]) == 1:
            temp_fire_balls.append(dict[key][0])
            continue
        # 같은 자리의 파이어볼이 2개 이상인 경우
        sum_m = 0 # 질량의 합
        sum_s = 0 # 속력의 합
        count = 0 # 짝수인 것의 개수
        for r,c,m,d,s in dict[key]:
            # 1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
            sum_m += m; sum_s += s
            if d % 2 == 0:
                count += 1
        # 파이어볼은 4개의 파이어볼로 나누어진다.
        # 1. 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        # 2. 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        r_m = sum_m//5; r_s = sum_s//len(dict[key])
        # 4. 질량이 0인 파이어볼은 소멸되어 없어진다.
        if r_m == 0:
            continue
        # 3. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
        if count == 0 or count == len(dict[key]):
            for dir in [0,2,4,6]:
                temp_fire_balls.append((r,c,r_m,dir,r_s))
        else:
            for dir in [1,3,5,7]:
                temp_fire_balls.append((r,c,r_m,dir,r_s))
    
    # 파이어볼 갱신
    fire_balls = temp_fire_balls
    
# 마법사 상어가 이동을 K번 명령한다.
while K > 0:
    move()
    K-=1

# 남아있는 파이어볼 질량 구하기
result = 0
for r,c,m,d,s in fire_balls:
    result += m

print(result)