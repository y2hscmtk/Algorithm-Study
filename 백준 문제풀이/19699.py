# https://www.acmicpc.net/problem/19699
'''
N개 중에 M개 선발
합이 소수인지 판별하여 소수라면 출력
'''
import sys
from math import sqrt
input = sys.stdin.readline
N,M = map(int,input().split())
cow = sorted(list(map(int,input().split()))) # 오름차순 출력을 위해 정렬
selected = [] # 선택된 소
result = []
# M개 선택
def select_cow(start):
    global selected,result
    # 재귀 탈출
    if len(selected) == M: # M마리의 소를 선별하였다면
        # 몸무게의 합이 소수인지 판별 -> 소수라면 출력
        SUM = sum(selected)
        # 1과 자기 자신을 제외하고 약수가 존재한다면 소수가 아님
        for i in range(2,int(sqrt(SUM))+1):
            if SUM%i==0: # 약수가 존재한다면 소수가 아님
                return
        # 여기까지 왔다면 소수
        if SUM not in result: # 아직 포함 안된 경우에 대해서만
            result.append(SUM)
    for i in range(start,N): # 중복 선택은 불가능함
        selected.append(cow[i]) # i번째 소 선택
        select_cow(i+1)
        selected.pop() # 백트래킹
select_cow(0) # 0번째 소부터 선택 시작
print(*sorted(result)) if len(result) else print(-1) # 정답 출력, 그러한 경우가 없다면 -1 출력