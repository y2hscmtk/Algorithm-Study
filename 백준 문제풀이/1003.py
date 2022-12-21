# https://www.acmicpc.net/problem/1003

# 피보나치 함수

'''
def fibonacci(n):
    global count0, count1, dp
    if dp[n] != 0:  # dp에 값이 저장되어 있는 상태라면
        return dp[n]  # dp에 저장된 값을 리턴
    else:  # 새로운 인덱스의 데이터라면 값 저장
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
새롭게 작성하거나, 혹은 반복문을 이용하여 값을 할당하는 방법을 고안할것
'''

'''
22/12/21 두번째 시도
시간복잡도 문제를 해결하기 위해, 재귀함수로 작성된 원본의 문제를
dp테이블에 기록하는 메모이제이션 기법을 이용한다.
'''


dp = [-1]*41  # n은 최개 40이므로
# 우리가 알고 있는 값은 미리 기록해둔다.
dp[0] = [1, 0]
dp[1] = [0, 1]

# 이후의 피보나치 수들은 다음의 점화식으로 표현이 가능하다
# fibo(n) = fibo(n-1) + fibo(n-2)
# 반복문을 돌면서 값을 기록하면 된다.

# 몇번 반복을 수행할 것인지 기록
t = int(input())

for _ in range(t):
    n = int(input())
    # 여기서 부터 fibo(n)에 대한 0과 1의 호출 횟수를 기록하기 위해 반복문 수행
    if n == 0 or n == 1:  # 0과 1에 대한 정보는 알고 있으므로
        count0 = dp[n][0]
        count1 = dp[n][1]
        print(count0, count1)
        continue  # 아래 반복문을 무시하고 다음 테스트 케이스로 넘어간다.
    # 0과 1이 아닌수에 대하여 계산을 수행할경우
    for i in range(2, n+1):  # 0과 1에 대한값은 이미 기록되어 있으므로
        if dp[i] != -1:  # 이미 값이 기록되어 있다면
            continue  # 다음수부터 기록 진행
        else:  # 값이 기록되기 전이라면
            count0 = dp[i-1][0] + dp[i-2][0]
            count1 = dp[i-1][1] + dp[i-2][1]
            dp[i] = [count0, count1]  # dp테이블에 값 기록
    # dp[n]의 값 출력
    count0 = dp[n][0]
    count1 = dp[n][1]
    print(count0, count1)
