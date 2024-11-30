# https://www.acmicpc.net/problem/1699
'''
dp[i] ; i를 제곱수의 합으로 표현할 때 필요한 최소 항의 개수
'''
from math import sqrt
# print(sqrt(100000)) # 316.2277..
# 317^2 이하의 제곱수로 100,000 표현 가능
dp = [float('inf')]*100001
for i in range(1,317):
    dp[i*i] = 1 # 1개의 제곱수가 필요한 경우를 기본값으로 초기화

for i in range(1,100001):
    if dp[i] != float('inf'):
        continue
    # 어떤 제곱수를 추가하는지에 따라 dp[i-1^2], dp[i-2^2]등 거슬러 올라가 최소 항의 개수 파악
    # 1^2,2^2,3^2등의 수가 추가되는 것이므로 +1 필요
    for j in range(1,int(sqrt(i))+1):
        dp[i] = min(dp[i],dp[i-(j*j)]+1)

print(dp[int(input())])