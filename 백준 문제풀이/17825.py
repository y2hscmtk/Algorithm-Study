# https://www.acmicpc.net/problem/17825
'''
처음에는 시작 칸에 말 4개가 있다.(말의 인덱스를 전부 -1로 둔다.)
말은 게임판에 그려진 화살표의 방향대로만 이동할 수 있다. 
파란색 칸(10,20,30)에서 이동을 시작하면 파란색 화살표를 타야 하고,
이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표를타야한다.
게임은 10개의 턴으로 이루어진다. 매 턴마다 1부터 5까지 한 면에 하나씩 있는 5면체 주사위를 굴리고,
도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수만큼 이동시킨다.
=> 주사위에서 나올 수는 이미 알고있다.(10개), 각각의 말이 현재 이동중인지 아닌지를 변수를 통해 저장
말이 이동을 마칠 때 마다 칸에 적혀있는 수가 점수에 추가 된다.
'''
import sys
route0 = [i for i in range(2,41,2)] # 일반적인 이동경로 2,4,6,..,40
route1 = [10,13,16,19,25,30,35,40] # 10의 파란색 화살표 경로
route2 = [20,22,24,25,30,35,40] # 20의 파란색 화살표 경로
route3 = [30,28,27,26,25,30,35,40] # 30의 파란색 화살표 경로
route = [route0,route1,route2,route3]
# 기본적인 루트에서 10,20,30의 인덱스는 각각 4,9,14
# 선택한 말의 도착지점이 route0에서 4,9,14가 될 경우 이동 루트와 인덱스를 변경한다.(인덱스 -> 0)
# index == 4 then route = route1, index = 0 ...
dice = list(map(int,input().split())) # 나올 수 있는 모든 주사위의 경우의 수
# 현재 말들의 상태
# 말의 위치(인덱스), 현재 이동중인 경로, 도착하였는지 아닌지
# 말들은 초기에 모두 시작(-1)지점에 위치한다.
player = [ [-1,0,False] for _ in range(4)]
result = -1 # 얻을 수 있는 포인트의 최대값
def move(curr,point): # curr은 현재 주사위의 번호
    global result,player,route
    # 주사위를 끝까지 다 돌았으면 최대값 갱신
    if curr == 10:
        result = max(result,point)
        return
    # 1. 현재 주사위만큼 이동할 말을 선택한다.
    # 1.1. 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다. 단 이동을 마치는 칸이 도착칸이면 고를 수 있다.
    # 말 선택은 브루트포스, n : 이동시킬 말의 번호
    for n in range(4): # 4개의 말에 대해서, 이동을 마치는 칸에 다른 말이 있는지 확인
        if player[n][2] == True: # 이동가능한 말인 경우에 한해
            continue # 이동가능한 말이 아니라면 넘어감
        next_pos = player[n][0] + dice[curr] # 다음에 이동할 위치
        next_route = player[n][1] # 현재 이동경로, 다음에 이동하게 될 경로    
        # 다음에 이동하게 될 위치 새롭게 지정
        if next_route == 0: # 0번째 경로에 대해서
            # 0번째의 4,9,14번은 1번째 경로의 0,2번째 경로의 0,3번째 경로의 0과 같은 위치에 해당
            if next_pos == 4:
                next_route = 1
                next_pos = 0
            elif next_pos == 9:
                next_route = 2
                next_pos = 0
            elif next_pos == 14:
                next_route = 3
                next_pos = 0
        # 가운데 지점인 25,30,35,40에서 또다시 경로가 겹친다.
        # 일치하는지 확인할 필요가 있다.
        # => 별도 처리가 필요하다.
        needToCheck = False
        if next_pos < len(route[next_route]): # 영역을 초과하지 않는 범위 한에서
            if route[next_route][next_pos] in [25,30,35,40] and next_pos != 0: # 경로 3의 0번째 값에도 30이 있음
                needToCheck = True # 조건식에서 검사가 필요함을 알림
        canMove = True
        # 다른 말들과 다음에 이동하게 될 경로가 겹치는지 검사
        for an in range(4): 
            if n == an:
                continue
            compare_pos = player[an][0]
            compare_route = player[an][1]
            isFinish = player[an][2]
            
            # 비교대상이 출발지에 있거나, 도착지에 있다면 무시
            if compare_pos == -1 or isFinish:
                continue
            # 같은 경로선상에 있으면서 위치가 같은 경우
            # 이동시키려는 말의 다음 위치에 말이 있으므로 이동 불가
            if next_route == compare_route and next_pos == compare_pos:
                canMove = False
                break # 한마리의 말이라도 해당 위치에 존재한다면 현재 말은 이동할 수 없다.
            # 이동하려는 칸과 같은 위치에 위치한다면
            if needToCheck:
                # compare_pos != 0을 하는 이유는 경로3의 0번째 인덱스의 경우 30이란 값이 있기 때문
                if route[compare_route][compare_pos] == route[next_route][next_pos] and compare_pos != 0:
                    canMove = False
                    break
            
        # 위 조건을 만족한다면 현재 말 n은 이동할 수 있는 말이다.
        if canMove:
            # 정보 저장(모든 말들에 대한 정보)
            copy_player = [p[:] for p in player]    
            score = 0 # 누적시킬 점수
            # 만약 현재 이동하려는 말이 이동경로를 초과해서 움직인다면 => '도착'지에 도달
            if next_pos >= len(route[next_route]):
                player[n][2] = True # 도착처리
            else: # 경로를 초과해서 움직이지 않는다면
                player[n][0] = next_pos
                player[n][1] = next_route
                score = route[next_route][next_pos] # 얻게 될 점수
            move(curr+1,point+score) # 말 이동
            player = copy_player # 백트래킹
move(0,0)
print(result)