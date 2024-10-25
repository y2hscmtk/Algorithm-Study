# https://www.acmicpc.net/problem/17615
'''
한번에 옮길 수 있는 공의 개수는 1개
같은색끼리 만드는 것이 목표 
-> 빨강색이든 파랑색이든 묶여있든 하나이든 결국 한쪽 끝으로 한 색을 모으는 것이 목표
<풀이참조>
# 1. 오른쪽 끝으로 공을 모으는 경우
# 2. 왼쪽 끝으로 공을 모으는 경우(오답 원인 : 오른쪽으로 공을 모으는 경우만 고려했었음)
두 경우를 구하여 최소값 출력
'''
result = []
import sys
input = sys.stdin.readline
N = int(input())
balls = list(map(str, input().strip()))
result = []

# 공을 오른쪽으로 밀 경우
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
result.append(red_count)
result.append(blue_count)

# 공을 왼쪽으로 밀 경우
red_count = 0; blue_count = 0 # 각 색깔공 최소 이동 횟수
last = balls[N-1] # 시작 공의 색상
count = 1
for i in range(N-2,-1,-1):
    if balls[i] == last:
        count += 1
    else: # 다른 색인 경우 -> 공이 분리된 경우
        if last == 'R':
            red_count += count # 지금까지 기록한 수 저장
        else:
            blue_count += count
        count = 1 # 현재 공에서부터 다시 카운팅
        last = balls[i] # 현재 색상의 공으로 변경
result.append(red_count)
result.append(blue_count)

print(min(result))