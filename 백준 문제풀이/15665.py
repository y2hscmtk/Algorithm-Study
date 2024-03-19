# https://www.acmicpc.net/problem/15665
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
def dfs(curr):
    if len(curr) == m: # M개의 수를 찾았으면 출력하고 재귀 종료
        print(*curr)
        return
    used = [False]*(max(numbers)+1) # 같은 수를 같은 자리에 사용할 수 없음
    for i in range(n):
        num = numbers[i]
        # 현재 자리에서 해당 숫자를 사용하지 않았다면
        if not used[num]:
            used[num] = True # 이번 자리에서 해당 숫자 사용처리
            curr.append(num) # 숫자 넣기
            dfs(curr)
            curr.pop() # 백트래킹
dfs([])