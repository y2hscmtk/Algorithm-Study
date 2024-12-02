# https://www.acmicpc.net/problem/1535
'''
풀이 참조 : 체력이 줄어드는 것이 조건이므로 역순으로 뒤에서부터 계산
    -> 사용한 체력(조건)
사람 
'''
N = int(input())
L = [0] + list(map(int,input().split()))
J = [0] + list(map(int,input().split()))

dp = [0]*101

for i in range(1,N+1):
    health,joy = L[i],J[i]
    # 체력이 0이하가 되면 안되므로 뒤에서부터 업데이트
    for current_health in range(100,health-1,-1):
        #                       인사를 하지 않는 경우, 인사를 하는 경우
        dp[current_health] = max(dp[current_health],dp[current_health - health] + joy)

print(max(dp[:100]))