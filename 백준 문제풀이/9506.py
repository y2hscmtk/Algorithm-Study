# https://www.acmicpc.net/problem/9506
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n==-1:
        break
    # 완전수 검사 시작
    # 자기 자신을 제외한 약수의 합이 자기 자신과 같다면 완전수
    temp = 1 # 1은 항상 약수임
    array = [] # 약수를 저장하기 위함
    for i in range(2,n//2+1): # 2부터 검사
        if n%i==0: # i가 n의 약수라면 temp에 더하기
            temp += i
            if temp > n: # n을 넘어선다면 완전수가 될 수 없음
                break
            array.append(i)
    if temp == n: # 완전수라면
        print(f'{n} = 1 + ',end='')
        for j in range(len(array)-1):
            print(f'{array[j]} + ',end='')
        print(array[-1])
    else:
        print(f'{n} is NOT perfect.')