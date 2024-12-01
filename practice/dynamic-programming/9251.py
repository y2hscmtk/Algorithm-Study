# https://www.acmicpc.net/problem/9251
'''
각 자리수별로 문자가 같은지 비교 
같다면 -> 기존에 비교했던 결과들 중 최대값 +1(현재 값도 일치)
같지 않다면 -> 기존에 비교했던 결과들 중 최대값
'''
arr1 = list(input())
arr2 = list(input())
dp = [[0]*(len(arr2)+1) for _ in range(len(arr1)+1)]

for i in range(1,len(arr1)+1):
    for j in range(1,len(arr2)+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[len(arr1)][len(arr2)])