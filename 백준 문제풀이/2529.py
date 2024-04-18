# https://www.acmicpc.net/problem/2529
'''
백트래킹, 브루트포스
0~9의 수들 중 수를 한 자리씩 넣는다. 선택된 숫자는 모두 달라야 한다.

여러분은 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다. 
단 아래 예(1)과 같이 첫 자리가 0인 경우도 정수에 포함되어야 한다. 
모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다. 

0~9까지 수들 중 겹치지 않도록 k+1개의 수를 뽑은 후, 부등호 관계가 맞는지 확인
조건을 만족하는 수라면 최소값과 최대값 갱신
'''
import sys
input = sys.stdin.readline
k = int(input())
inequality = list(input().split())
selected = [-1 for _ in range(k+1)]
used = [False]*10 # used[9] => 9번 숫자를 사용한 것을 의미
result = []

# 지금까지 선택된 수들이 부등호 조건을 만족하는지 확인
def isSuccess():
    for i in range(len(inequality)):
        eq = inequality[i]
        if eq == '<' and selected[i] > selected[i+1]:
            return False
        elif eq == '>' and selected[i] < selected[i+1]:
            return False
    return True


def dfs(x):
    global used,selected
    if x == k+1: # k+1 개의 숫자를 선택하면 탈출
        if isSuccess(): # 조건 확인
            result.append(''.join(map(str,selected)))
        return
    
    # 이미 선택된 숫자는 선택하지 않되, 순서는 달라져야한다.
    for i in range(10): # 0~9
        if not used[i]: # i번 사용 가능한 경우에 대해서
            used[i] = True # 사용처리
            selected[x] = i # x번째 수를 i로 선택
            dfs(x+1)
            # 백트래킹
            selected[x] = -1 
            used[i] = False 

dfs(0)
result.sort()
print(result[-1])
print(result[0])