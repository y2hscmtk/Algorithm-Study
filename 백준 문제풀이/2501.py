# https://www.acmicpc.net/problem/2501
'''
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
'''
import sys
n, k = map(int, input().split())

count = 0
for i in range(1, n+1):
    if n % i == 0:  # 만약 i가 n의 약수라면
        count += 1  # 약수를 하나 찾았다는 의미로 카운트 증가
        # 그리고 그 약수가 k번째로 작은 수라면 출력
        if count == k:
            print(count)
            sys.exit(0)  # 프로그램 종료
print(0)  # 약수를 찾지 못하였다면 프로그램 종료
