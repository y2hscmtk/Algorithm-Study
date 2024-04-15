# https://www.acmicpc.net/problem/20056
'''
1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어있다??

마법사 상어가 모든 파이어볼에게 이동을 명령한다.
1. 모든 파이어볼이 자신의 방향 d로 s칸 만큼 이동한다.
    => 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수 있다. -> 2번 수행
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 아래와 같은 일이 발생한다.
    1. 같은 칸에 있는 파이어볼은 모두 한 개로 합쳐진다. => 4번 항목 검사
    2. (합쳐진 후)파이어볼은 4개의 파이어볼로 나누어진다.
    3. 나누어진 파이어볼의 질량, 속도, 방향은 다음과 같다.
        1. 질량은 [합쳐진 파이어볼의 질량의 합/5]이다.
        2. 속력은 [합쳐진 파이어볼의 속력의 합/합쳐진 파이어볼의 개수]이다.
        3. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수이면 방향은 0,2,4,6이 되고, 그렇지 않으면 1,3,5,6
    4. 질량이 0인 파이어볼은 소멸되어 없어진다.

마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구하라
'''
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
# 파이어볼 방향 0~7번 방향
direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
# N x N 크기의 맵에 파이어볼 M개 발사 => N x N 크기의 배열 생성
# 수행에 영향을 끼치는 정보는 질량, 속력, 방향 => 3가지에 대한 배열 생성
fire_balls = [[] for _ in range(M)] # 파이어볼은 M개

data = {} # 파이어볼의 임시 정보를 저장하기 위한 dict

# 파이어볼에 대한 정보 입력받기
for i in range(M):
    r,c,m,s,d = map(int,input().split())
    r-=1;c-=1
    fire_balls[i] = [r,c,m,s,d] # 파이어볼 정보 입력받기


# 1. 이동하는 함수
# 모든 파이어볼이 자신의 방향 d로 s칸 만큼 이동한다. => 이동하는 중에는 한 칸에 여러개의 파이어볼이 있을 수 있다.
def move(r,c,m,s,d):
    global data
    # 만약 현재 파이어볼의 질량이 0이라면 소멸되어 없어진다.
    if m != 0: # 질량이 0이 아니라면
        # 다음 좌표는 모듈러 연산으로 이동
        nr = (r+direction[d][0]*s)%N
        nc = (c+direction[d][1]*s)%N
        key = f'{nr}-{nc}'
        if key in data:
            data[key].append([nr,nc,m,s,d]) # 질량,속도,방향 삽입
        else:
            data[key] = [[nr,nc,m,s,d]]

# 2. 파이어볼 합치기 함수
def plus_fireballs():
    global fire_balls,data
    # 모든 배열을 돌면서 임시 저장소에 있는 파이어볼에 대해서 합치기 수행
    temp = [] # 흩어지는 파이어볼의 다음 위치
    for key in data:
        sum_m = 0 # 질량의 합
        sum_s = 0 # 속력의 합
        count = len(data[key])
        h,z = 0,0 # 홀,짝
        for r,c,m,s,d in data[key]:
            # 질량은 모두 0이 아님이 보장되어있음
            sum_m += m; sum_s += s
            # 방향이 모두 짝수인지 검사
            if d%2==0:
                z+=1
            else:
                h+=1
        # 새로운 질량 = 합쳐진 파이어볼 질량의 합/5
        new_m = sum_m//5
        # 새로운 속력 = 합쳐진 파이어볼의 속력의 합/합쳐진 파이어볼의 개수
        new_s = sum_s//count
        # 방향이 모두 홀수거나 짝수이면
        if h==count or z==count:
            # => 흩어지는 파이어볼의 방향은 0,2,4,6이 된다.
            for k in range(0,7,+2): # 다음 위치
                nr = (r + direction[k][0])%N
                nc = (c + direction[k][1])%N
                temp.append([nr,nc,new_m,new_s,k])
        else: # => 그렇지 않으면 1,3,5,7이 된다.
            for k in range(1,8,+2): # 다음 위치
                nr = (r + direction[k][0])%N
                nc = (c + direction[k][1])%N
                temp.append([nr,nc,new_m,new_s,k])
    # temp를 새로운 fire_balls로 설정
    fire_balls = temp

    
# 알고리즘
for _ in range(K): # 마법사의 명령은 K번 수행된다.
    # 1. 모든 파이어볼이 이동
    for fireball in fire_balls:
        r,c,m,s,d = fireball
        move(r,c,m,s,d)
    # 2. 같은 위치의 파이어볼 합치기
    plus_fireballs()
    data = {} # 이동이 끝난 이후에는 임시 저장소 초기화

# 남아있는 파이어볼 질량의 합 구하기
result = 0
for r,c,m,s,d in fire_balls:
    result += m

print(result)    