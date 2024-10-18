# https://www.acmicpc.net/problem/11508
'''
3개씩 묶어서 살 때, 3개의 값 중 가장 싼 값을 할인해줌
1. 3개씩 몇개 묶음이 되는지 계산
-> 내림차순 정렬 후, 앞에서부터 바구니 채워 나가기 -> 가장 큰 값을 할인하는것이 이득이므로
2. 이후 남은 숫자는 그냥 계산
풀이참조 : x
'''
import sys
input = sys.stdin.readline
price = []
# 가격 입력받기
for _ in range(int(input())):
    price.append(int(input()))
total_price = sum(price) # 총 결제 금액

price.sort(reverse=True) # 내림차순 정렬
# 일단 3개씩 묶어서 할인 받을 수 있는 값은 할인 받는 것이 무조건 이득
# 내림차순 정렬후 3번째 있는 값들을 할인 받을 때가 가장 할인 받는 경우
for i in range(2,len(price),3):
    total_price -= price[i]

print(total_price)