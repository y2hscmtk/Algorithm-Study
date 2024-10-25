# https://www.acmicpc.net/problem/17615
'''
한번에 옮길 수 있는 공의 개수는 1개
같은색끼리 만드는 것이 목표 
-> 빨강색이든 파랑색이든 묶여있든 하나이든 결국 한쪽 끝으로 한 색을 모으는 것이 목표
'''
N = int(input())
balls = input()
# 빨간색 공, 파란색 공 연결된 위치 각각 입력받기
last = balls[0]; group = [0,0] # 공 시작 위치
red_ball = []; blue_ball = []
for i in range(N):
    ball = balls[i]
    if ball == last: # 이전과 같은 색 공이라면 -> 이어져 있다면
        group[1] = i # 공 위치 저장
        if i == N-1:
            red_ball.append(group) if last == 'R' else blue_ball.append(group)
    else: # 이전과 다른색 공이라면 -> 연결이 끊어짐
        red_ball.append(group) if last == 'R' else blue_ball.append(group)
        last = ball
        group = [i,i] # 그룹 초기화

# 빨간색 공에 대해서
red_count = 0
for x,y in red_ball:
    # 이미 끝자리에 위치하는 경우는 공을 이동할 필요 없음
    if y == N-1:
        continue
    # 공은 한번에 한개씩 이동 가능
    # for i in range(x,y+1):
    #     red_count += 1
    red_count += (y-x+1) # 각각의 공을 모두 옮길 것이므로

# 파란색 공에 대해서
blue_count = 0
for x,y in blue_ball:
    if y == N-1:
        continue
    blue_count += (y-x+1)

print(min(red_count,blue_count))