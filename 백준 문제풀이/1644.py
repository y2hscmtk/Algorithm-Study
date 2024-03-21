# https://www.acmicpc.net/problem/1644
'''
1. 소수를 먼저 찾아서 배열에 넣어놓는다.
2. 배열의 값들을 대상으로 투 포인터를 사용하여 조건을 만족하는 경우의 수 파악
'''
from math import sqrt
N = int(input())
# 2~N까지의 소수 판정 수행
if N<2: # 1은 소수가 아님
    print(0)
else: # N>=2
    prime = [2]
    for i in range(3,N+1,+2): # 2를 제외한 짝수는 소수가 될 수 없다.(전처리)
        isPrime = True
        for j in range(3,int(sqrt(i))+1,+2): # i는 짝수가 아니므로 홀수에 대해서만 탐색하면됨
            if i%j==0: # 1과 자기 자신을 제외하고 나누어 떨어지는 수가 존재한다면 소수가 될 수 없다.
                isPrime = False
                break
        if isPrime: # 판정 결과 소수라면
            prime.append(i)
    
    # 투 포인터를 활용하여 생성된 소수 배열을 통해 원하는 수를 만들 수 있는지 파악
    start,end,result = 0,0,0
    while True:
        # 끝까지 다 돌았다면 종료
        if end == len(prime):
            break
        suM = sum(prime[start:end+1])
        if suM == N:  # 원하는 수를 만들었다면 
            result+=1 # 정답 +1
            start+=1 # 시작 칸 한칸 앞으로 이동
        elif suM < N: # 아직 부족하면
            end+=1 # 끝 칸 한칸 앞으로 이동
        else: # suM > N
            start+=1 # 시작 칸 한칸 앞으로 이동
    print(result)
