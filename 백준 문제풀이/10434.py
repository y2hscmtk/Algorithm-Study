# https://www.acmicpc.net/problem/10434
'''
수가 주어질 때, 각 수가 행복한 소수인지 여부 판단
'''
import sys
from math import sqrt

# 에라토스테네스의 체
isPrime = [True for _ in range(10001)] 
isPrime[1] = False # 이 문제의 경우 1은 소수로 분류하지 않는다.

for i in range(2,int(sqrt(10001))+1):
    # 에라토스테네스의 체에 소수로 등록된 수라면, 해당 수의 배수를 1000이하의 수까지 지운다.
    if isPrime[i]:
        j = 2
        while i*j<10001:
            isPrime[i*j] = False # 소수가 아님
            j+=1
            
def isHappy(n):
    # n이 행복한 소수인지 판정
    check = [] # 무한 반복 방지용
    while True:
        # 각 자리수의 제곱의 합이 1이 된다면 행복한 수
        arr = []
        if 1000<=n: # 네자리 수 라면
            arr.append(n//1000)
            n %= 1000
            arr.append(n//100)
            n %= 100
            arr.append(n//10)
            arr.append(n%10)
        elif 100<=n<1000: # 세자리 수 라면
            arr.append(n//100)
            n %= 100
            arr.append(n//10)
            arr.append(n%10)
        elif 10<=n<100: # 두자리 수 라면
            arr.append(n//10)
            arr.append(n%10)
        elif 1<=n<10: # 한자리 수 라면
            arr.append(n)
        # 각 자리 수 제곱해서 확인
        n = 0
        for num in arr:
            n += num**2
        if n == 1:
            return True
        if n in check:
            return False
        check.append(n) # 무한반복 방지 => 같은 수 재등장시 행복한 수가 될 수 없음

# 행복한 소수 판정
# 테스트케이스 입력받기
for _ in range(int(input())):
    num,n = map(int,input().split())
    # 소수라면
    if isPrime[n]:
        # 행복한 소수인지 판정 
        if isHappy(n):
            print(num,n,"YES")
        else:
            print(num,n,"NO")
    else:
        print(num,n,"NO")
