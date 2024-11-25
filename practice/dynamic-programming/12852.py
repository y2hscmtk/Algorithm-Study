# https://www.acmicpc.net/problem/12852
'''
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
'''
dp = [[] for _ in range(10**6 + 1)]
dp[1],dp[2],dp[3] = [1],[2,1],[3,1]
for i in range(4,10**6+1):
    # 1을 빼는 경우
    dp[i] = [i] + dp[i-1] # 현재 수, 현재수-1를 1로 만드는 방법
    if i%3 == 0 and len([i] + dp[i//3]) < len(dp[i]): # 더 짧아진다면 갱신
        dp[i] = [i] + dp[i//3] # 현재수, 3으로 나눈 수를 1로 만드는 방법
    if i%2 == 0 and len([i] + dp[i//2]) < len(dp[i]): # 더 짧아진다면 갱신
        dp[i] = [i] + dp[i//2] # 현재수, 2로 나눈 수를 1로 만드는 방법
    

n = int(input())
print(len(dp[n])-1)
print(*dp[n])
