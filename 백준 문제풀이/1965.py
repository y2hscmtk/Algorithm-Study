# https://www.acmicpc.net/problem/1965
'''
가장 긴 증가하는 부분수열 문제
dp테이블을 만들어서 현재시점에서의 길이를 저장하고
dp에서의 max값을 정답으로 출력
'''
n = int(input())
numbers = list(map(int,input().split()))
dp = [0]*n
dp[0] = 1 # 첫번째 수는 무조건 선택함

# 현재 자리수 이전의 자리 수와 대소 비교
# 현재 수가 이전 수보다 더 크다면, dp에 누적된 자리수 확인 후 업데이트
for i in range(1,n):
    for j in range(i):
        # 현재수(numbers[i])와 비교해서 더 작은 수인지 확인
        # 더 작은 수라면 누적된 자리수가 더 긴지 확인(그 이전까지의 숫자들은 포함할수 있음)
        if numbers[j] < numbers[i] and dp[i] < dp[j]:
            dp[i] = dp[j] # 이전 수 중에서 가장 길이를 길게 한 수만큼의 길이는 포함할 수 있으므로
    dp[i] += 1 # 현재 수 자기 자신의 길이를 포함하기 위함

print(max(dp))
