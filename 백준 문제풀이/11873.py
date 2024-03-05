# https://www.acmicpc.net/problem/11873
'''
1로 이루어진 가장 큰 직사각형 찾기
'''
import sys
input = sys.stdin.readline

def find_max_rectangle(row):
    temp = 0 # 사각형
    stack = []
    for index,height in enumerate(row):
        keep = index
        while stack and stack[-1][1] > height:
            i,h = stack.pop() # i~index에는 모두 높이가 h이상임이 보장됨
            temp = max(temp,(index-i)*h)
            keep = i
        stack.append((keep,height)) # keep부터 가장 최신의 막대까지는 모두 높이가 height이상임이 보장됨
    # 남아있는 값들에 대해서
    for index,height in stack:
        # 현재 인덱스부터 끝까지는 모두 높이가 height 이상임이 보장됨
        temp = max(temp,(len(row)-index)*height)
    return temp

while True:
    n,m = map(int,input().split())
    if (n,m) == (0,0):
        break
    data = [list(map(int,input().split())) for _ in range(n)]
    for i in range(1,n): # 1번째 줄 부터 시작
        for j in range(m):
            if data[i][j] == 1 and data[i-1][j] != 0: # 이전 숫자가 0이 아니라면
                data[i][j] = data[i-1][j] + 1
    # 모든 행에 대해서 가장 큰 직사각형 알고리즘 수행
    result = 0
    for row in data:
        result = max(result,find_max_rectangle(row))
    print(result)
