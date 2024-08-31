# https://www.acmicpc.net/problem/16922
'''
사용가능한 수 1,5,10,50
1,5,10,50은 무한히 존재함
순서는 신경쓰지 않으며, 만들 수 있는 모든 수의 개수 출력
1 <= N <= 20
50*20 = 1000, 최대 1000 제작 가능
'''
import sys
input = sys.stdin.readline
N = int(input())
numbers = [1,5,10,50]
isMake = [False for _ in range(1001)]
num = 0
# 1,5,10,50 중에 수 선택
def dfs(depth,start):
    global num
    # N개의 수를 골랐으면 탐색 종료    
    if depth == N:
        # 현재까지 선택한 수를 모두 더하고 true로 변경
        isMake[num] = True
        return
    for i in range(start,4):
        # 아라비아 숫자들 중 하나 선택
        num += numbers[i]
        dfs(depth+1,i)
        num -= numbers[i] # 백트래킹
dfs(0,0)
# 제작된 수 모두 출력
print(isMake.count(True))