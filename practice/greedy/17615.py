# https://www.acmicpc.net/problem/17615
'''
한번에 옮길 수 있는 공의 개수는 1개
같은색끼리 만드는 것이 목표 
-> 빨강색이든 파랑색이든 묶여있든 하나이든 결국 한쪽 끝으로 한 색을 모으는 것이 목표
<15점>
파란색공, 빨간색 공 위치 분리 후 각 공에 대해서 한쪽 끝으로 이동하기 각각 수행 이후 최소값 출력
<15점>
시간초과 판정을 줄이기 위해 공을 구분하면서 이동하는 과정을 한번에 수행
-> 각 색깔 공이 이어져있는 수 카운팅(마지막까지 이어져있는 경우는 무시(이동할 필요x))
-> 시간 단축 성공, 여전히 15점
'''
N = int(input())
balls = input()
red_count = 0; blue_count = 0 # 각 색깔공 최소 이동 횟수
last = balls[0] # 시작 공의 색상
count = 1
for i in range(1,N): # 두번째 공부터 끝 공까지 비교 시작
    if balls[i] == last:
        count += 1
    else: # 다른 색인 경우 -> 공이 분리된 경우
        if last == 'R':
            red_count += count # 지금까지 기록한 수 저장
        else:
            blue_count += count
        count = 1 # 현재 공에서부터 다시 카운팅
        last = balls[i] # 현재 색상의 공으로 변경

print(min(red_count,blue_count))