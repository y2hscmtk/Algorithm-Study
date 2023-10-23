# https://www.acmicpc.net/problem/2942
'''
아이디어 : 
1.유클리드 호제법을 사용하여 두 수의 최대 공약수를 구한다.
2.최대 공약수를 이용하여 두 수의 공약수들을 구한다.
3.공약수배열을 사용하여 정답을 출력한다.
'''
import sys
from math import sqrt
R,G = map(int,input().split())


def find_gcd(m,n):
	if m < n:
		m,n = n,m
	if n == 0: # 나누어 떨어진 경우
		return m
	if m % n == 0:
		return n
	else:
		return find_gcd(n, m%n)
	
gcd = find_gcd(R,G) # 최대 공약수 찾기
# 약수 파악
for i in range(1,int(sqrt(gcd))+1):
	if gcd%i == 0:
		if int(gcd/i)==i:
			print(i,int(R/i),int(G/i))
		else:
			print(i,int(R/i),int(G/i))
			print(int(gcd/i),int(R/int(gcd/i)),int(G/int(gcd/i)))
            
