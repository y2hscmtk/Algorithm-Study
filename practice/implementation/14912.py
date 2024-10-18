# https://www.acmicpc.net/problem/14912
'''
예상 풀이 방법
n이하의 수 중에서 d가 몇번 들어가는지 누적 카운팅 후 출력
16:20 ~ 
'''
n, d = map(int,input().split())

dp = [0]*(n+1)

for i in range(1,n+1):
    # 현재 수에 d가 몇번 들어가는지 카운팅
    num = str(i)
    count = 0
    for j in range(len(num)):
        if int(num[j]) == d:
            count += 1            
    dp[i] = dp[i-1] + count

print(dp[n])