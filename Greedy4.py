# 1이 될 때까지

#어떠한 수 N이 1이 될 떄까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.
#단 두번째 연산은 N이 k로 나누어떨어질 때만 선택할 수 있다.

#1. N에서 1을 뺀다.
#2. N을 K로 나눈다.

#다음과정을 최소 횟수로 수행하여 1을 만들면 성공

#아이디어 : 2번 과정을 최대한 많이 수행하고 1번 과정을 최소로 수행하면 된다.

#입력조건 : 첫째줄에 N과 K가 공백으로 구분되어 각각 자연수로 주어진다. 이때 N은 항상 K보다 크거나 같다.
#출력 : 수행하는 최소횟수를 출력한다.

import time

n,k=map(int,input().split())

time_1 = time.perf_counter()
count=0
while n!=1:
    if n%k==0: #n이 k의 배수라면?
        count+=1
        n//=k
    else:
        count+=1
        n-=1
time_2 = time.perf_counter()
print(count)
time_interval = time_2 - time_1
print(time_interval)