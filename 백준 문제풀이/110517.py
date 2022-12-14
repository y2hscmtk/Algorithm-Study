# https://www.acmicpc.net/problem/11057

'''
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.

첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

'''

'''
아이디어 : 같거나 오름차순으로 이어진 수는 오르막 수이다.
1자리수일때의 오르막수의 개수, 2자리 수일때의 오르막 수의 개수 등을 dp에 저장한다.

+) 앞자리 수가 0인 2자리 수의 오르막 수의 개수는 0/0~9 로 10개, 앞자리 수가 1인 2자리 수의 오르막 수의 개수는 1/1~9로 9개 ...등
'''

n = int(input())

# dp테이블 생성
# n자리수까지 고려
dp = [[0]*10 for _ in range(1001)]

# 1자리 수의 경우는 0~9로 10개이다.
dp[1] = 10
# 2자리 수의 경우는 앞자리 수에 따라 달라진다.
for i in range(10):  # 앞자리 수는 0~9가 될 수 있다.
    # 앞자리수가 i일때의 2자리 수의 오르막수의 개수는 다음과 같이 표현한다.
    dp[2][i] = (dp[1] - i)

# 3자리수 이상부터 알고리즘시작(2자리수까지는 이미 계산되어있으므로)
for k in range(3, n+1):  # n자리수까지 작동
    for i in range(10):  # 앞자리 수는 0~9가 될 수 있다.
        for j in range(i, 10):
            dp[k][i] += (dp[k-1][j] % 10007)  # 모듈러 연산시행하여 저장(오버플로우 방지)

# 정답 출력
if n == 1:
    print(10)
else:
    print(sum(dp[n]) % 10007)
