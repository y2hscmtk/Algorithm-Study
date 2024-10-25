# https://www.acmicpc.net/problem/17521
'''
저점일때 사서 고점일때 매수
-> 뒤에서부터 고점과 저점을 기록해두고 다시 앞에서부터 매수 매도 반복
<코드 풀이 참조>
'''
import sys
input = sys.stdin.readline
n,w  = map(int,input().split())
coin = []
cnt = 0
for _ in range(n):
	coin.append(int(input()))

for i in range(n-1):
	if coin[i] < coin[i+1]: # 증가 비교
		if w // coin[i] > 0: # 구매할 수 있는 코인이 남아있다면 현재 시점이 최저점임을 의미
			cnt = w // coin[i]
			w = w % coin[i]
	# 감소 비교 - 현재시점이 고점이라면 코인 판매(이후의 값보다 현재 값이 더 크다는 것은 이전 조건식을 통해 증명)
	elif coin[i-1] < coin[i]: 
		w += cnt*coin[i]
		cnt = 0
# 마지막 값에 대해서 잔여 코인 매수
if cnt != 0:
	w += cnt*coin[-1]
print(w)