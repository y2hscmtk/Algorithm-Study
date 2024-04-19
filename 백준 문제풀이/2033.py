# https://www.acmicpc.net/problem/2023
'''
신기한 소수는 각 자리의 수가 모두 소수인 수를 말한다.
1<=N<=8
각 자리의 수가 소수가 되려면 짝수는 어차피 불가능
'''
from math import sqrt
import sys
input = sys.stdin.readline

N = int(input())
number = []

def isPrime(num):
    target = int(''.join(map(str,number)) + str(num))
    if target == 1:
        return False
    if target == 2:
        return True
    if target%2 == 0:
        return False
    # 2이후의 홀수에 대해서 나눠지는지 확인
    for i in range(3,int(sqrt(target))+1,2): 
        if target%i==0:
            return False
    return True
    
def dfs(size):
    if size == N: # N자리가 되었다면 출력
        print(''.join(map(str,number)))
        return
    for i in range(1,10):
        # i를 추가함으로서 현재 자리수가 짝수가 되는지 확인(이전 수에 대해서는 이전에 검사함)
        if isPrime(i):
            number.append(i)
            dfs(size+1)
            number.pop()
            
dfs(0)