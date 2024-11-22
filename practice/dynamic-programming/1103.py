# https://www.acmicpc.net/problem/1003
'''
f(0) = 0
f(1) = 1
f(2) = 0 + 1
f(3) = (1) + (0+1)
...
피보나치 수를 반복할 때 마다, 0과 1의 저장 횟수를 누적하여 저장
풀이참조 : X
'''
dp = [[0 for _ in range(2)] for _ in range(41)]  # 피보나치 수 40까지 미리 기록
dp[0],dp[1] = [1,0],[0,1] 
for i in range(2,41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in range(int(input())):
    print(*dp[int(input())])
    