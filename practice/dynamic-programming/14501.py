# https://www.acmicpc.net/problem/14501
'''
상담을 하는 경우, 상담을 하지 않는 경우
'''
import sys
input = sys.stdin.readline

result = []

def dfs(day, price):
    # 정해진 날짜를 초과할 경우 상담 불가
    if day > N+1:
        return
    result.append(price) # 현재까지 얻은 최대 수익 저장
    # 1. 해당 요일에 상담을 하는 경우
    if day <= N:
        dfs(day+T[day], price+P[day])
    # 2. 해당 요일에 상담을 하지 않는 경우
    dfs(day+1,price) # 다음 날로 이동

N = int(input())
T = [0]*(N+1)
P = [0]*(N+1)
for i in range(1,N+1):
    ti,pi = map(int,input().split())
    T[i],P[i] = ti,pi

dfs(1,0)
print(max(result))