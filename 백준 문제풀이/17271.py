# https://www.acmicpc.net/problem/17271
'''
n개의 상자를 m의 크기를 가진 상자와, 1의 크기를 가진 상자로 채운다고 생각해보자
문제의 예시상황에서 n = 4, m = 2일때
dp[1] = A
dp[2] = AA,B
dp[3] = (AA,B) + A, AB
dp[4] = (AAA,BA,AB) + A, AAB, BB 
로 표현이 가능하며, 마지막에 놓을 상자가 A(크기1)인지 B(크기 m)인지에 따라
dp[i] = dp[i-1] + dp[i-m]과 같은 점화식을 만들 수 있다.
dp[i-1] : 이전상자 조합의 끝에 A를 늫아야 하므로
dp[i-m] : 마지막 상자에 m을 놓기 위해선 m만큼의 크기가 비워져야 하므로
'''
# 가능한 조합의 수를 1,000,000,007로 나눈 나머지 값을 출력한다.
n, m = map(int, input().split())

'''
dp[i] = dp[i-1] + dp[i-m]
i = 1, dp[1] = dp[0] + dp[1-m]
=> 즉 dp[m]까지는 작성이 되어 있어야함
'''
dp = [0]*(n+1)  # 0부터 n번째 인덱스까지 dp생성
dp[1] = 1
# 메모이제이션
for i in range(1, n+1):
    if i < m:
        dp[i] = 1
    elif i == m:
        dp[i] = dp[i-1] + 1  # 1은 m 하나를 기록하는 경우에 해당
    else:
        dp[i] = dp[i-1] + dp[i-m]

print(dp[n] % 1000000007)
