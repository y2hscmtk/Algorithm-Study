# https://www.acmicpc.net/problem/1990
'''
팰린드롬인지 먼저 판별,
그 이후에 소수인지 판별
두 조건을 모두 만족한다면 출력
'''
import sys
from math import sqrt
input = sys.stdin.readline

a, b = map(int, input().split())

# 전처리 (짝수는 소수가 될 수 없음)
# 홀수에서 부터 시작할 수 있도록
if a % 2 == 0:
    a += 1
# b = math.sqrt(b)

# a와 같거나 큰 홀수들 i에서 아래 조건 확인
# 1. 팰린드롬인지, 2. 홀수 인지
# a이상 b이하의 수 중에서 팰린드롬이면서 소수인 수 출력
for i in range(a, b+1, +2):
    # 팰린드롬 판별
    check = str(i)
    pel = True  # 팰린드롬인지 아닌지
    for j in range(len(check)//2):
        if check[j] != check[len(check)-j-1]:
            pel = False
            break
    # 만약 팰린드롬이라면, 소수판별 진행
    if pel:
        pri = True
        for j in range(3, int(sqrt(i))+1, +2):
            if i % j == 0:  # 1과 i 이하에 i의 약수 j가 존재한다면, i는 소수가 아님
                pri = False  # 소수 아님
                break
        if pri:  # 소수라면
            print(i)
print(-1)  # 마지막엔 -1출력
