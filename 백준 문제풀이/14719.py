# https://www.acmicpc.net/problem/14719
'''
가장 밑에서 부터 한 줄 씩 카운트하면 될듯?
빗물이 고일 수 있는 조건 물이 있는 공간의 왼쪽과 오른쪽이 블럭으로 채워져 있어야 함
'''
import sys
input = sys.stdin.readline
H,W = map(int,input().split())
data = list(map(int,input().split()))
# 2차원 배열 생성
block = [[False]*W for _ in range(H)]
# 블록 세우기
for i,b in enumerate(data): # i번째 열에 놓여져 있는 블럭의 수 b
    for j in range(H-b, H):
        block[j][i] = True # 블럭 세우기

# 가장 마지막 줄에서부터, 물의 개수 카운트
result = 0
for i in range(H-1,-1,-1): # 가장 마지막 행에서부터 시작
    water = 0 # 해당 행에 존재하는 물의 수 카운팅
    lastIsWater = False # 이전 칸에 물이었는지 아닌지 확인하기 위함
    for j in range(W):
        if block[i][j]: # 해당 위치에 블럭이 있다면
            # 이전까지 계산한 물의 수 정답에 누적
            result += water
            water = 0 # 물 양 초기화
            lastIsWater = False # 현재 칸은 블럭임
            continue # 다음 칸으로 넘어가기
        else: # 현재 칸에 블럭이 없다.
            # 현재 칸이 마지막 칸이면서, 물이 0이 아니다 => 물을 저장할 수 없다.
            if j == W-1 and water != 0:
                water = 0
            # 처음 칸이 아니면서, 이전칸에 블럭이 있거나 물이다.
            elif j!= 0 and (block[i][j-1] or lastIsWater):
                water += 1
                lastIsWater = True # 현재 칸이 물임을 다음칸에 전달

print(result)