# https://www.acmicpc.net/problem/2247

'''
실질적 약수는 1과 자기 자신을 제외한 모든 약수를 가리킨다.
SOD는 실질적약수의 합을 가리킨다
예를 들어 SOD(6) = 2 + 3 = 5이고, SOD(13) = 0 이다
.
CSOD(n)은 SOD(1) + SOD(2) + … + SOD(n)이라고 하자.
CSOD(n)을 구하는 프로그램을 작성하시오.
1 ≤ n ≤ 200,000,000
'''
'''
<아이디어>
1부터 n까지의 수를 거쳐가면서
소수의 경우 SOD(13)이므로 SOD계산을 수행하지 않고
소수가 아닌 경우, SOD연산을 수행하여 합을 더한다.
소수 판별, 약수 찾기
약수 찾기는 루트까지만 계산, 약수를 찾으면 약수와 몫을 더한 수를 정답에 누적
'''
from math import sqrt
result = 0
n = int(input())

# 소수 판별 함수
def isPrime(n):
    # 2보다 작거나 같은 수는 소수가 아니다.
    # 짝수는 소수가 아니다. => 짝수인 경우는 CSOD에서 걸러진다.
    # 3 이상의 모든 홀수들 중에서 소수를 판별 시작
    for i in range(3,int(sqrt(n))+1,+2): # sqrt(n)까지 나누어떨어지는 수가 있는지 검사
        if n % i == 0:
            return False # 존재한다면 소수가 아님
    return True


# CSOD를 구하는 함수
def CSOD(n):
    global result
    # 1,2,3는 SOD = 0()
    for i in range(4,n+1):
        # 짝수인 경우는 소수가 아니므로, 무조건 SOD가 0이상이다.
        if i%2==0: # 짝수인 경우에는
            result += SOD(i) # SOD연산을 수행한다.
        else: # 홀수인 경우, 소수인지 검사하고, 소수가 아니라면 SOD를 수행한다.
            # 소수 판별
            if not isPrime(i): # i가 소수가 아닌경우
                result += SOD(i) # SOD연산을 수행한다.
                
# SOD를 계산하는 함수
# SOD(n) => 1과 n을 제외한, n의 모든 약수들의 합
def SOD(n):
    temp = 0
    for i in range(2,int(sqrt(n))+1): # sqrt(n) 까지
        s = n//i # 몫
        r = n % i # 나머지
        if r == 0: # 나머지가 0이라면, i는 n의 실질적 약수
            # 몫과 같지 않은 경우에만
            if i!=s: # 4의 약수 = 1,2,4 => 2를 2번 더하는 경우가 생길 수 있으므로
                temp += (i + s) # 몫과 나누는 수가 약수에 해당함
            else: # 같다면 한번만 더하기
                temp += i
    return temp


CSOD(n)
# CSOD(n)을 1,000,000으로 나눈 나머지를 출력한다.
print(result%1000000)
