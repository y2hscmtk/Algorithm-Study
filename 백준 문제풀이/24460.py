# https://www.acmicpc.net/problem/24460
'''
1. 특별상을 받을 수 있는 사람이 한 명이라면, 그 사람이 뽑힌다.
2. 그렇지 않은 경우, 대회장을 같은 크기의 정사각형 네 개로 나누어 각 구역에서 이 규칙을 재귀적으로 적용해서 구역마다 한 명씩 총 네 명을 뽑는다.
3. 뽑힌 네 명 중 의자에 적힌 추첨번호가 두 번째로 작은 사람이 뽑힌다.
'''
def recursion(s,e,depth):
    if depth == 1: # 특별상을 받을 수 있는 사람이 한 명이라면, 그 사람이 뽑힌다.
        return data[s][e]
    # 정사각형 각 모서리에서 뽑힌 수들중 두번째로 작은 숫자가 뽑힌다.
    half = depth//2
    numbers = []
    # 왼쪽 위 모서리
    numbers.append(recursion(s,e,depth//2))
    # 오른쪽 위 모서리
    numbers.append(recursion(s,e+half,depth//2))
    # 왼쪽 아래 모서리
    numbers.append(recursion(s+half,e,depth//2))
    # 오른쪽 아래 모서리
    numbers.append(recursion(s+half,e+half,depth//2))
    numbers.sort()
    return numbers[1] # 두번째로 작은 수를 반환

N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]
print(recursion(0,0,N))