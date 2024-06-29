# https://www.acmicpc.net/problem/11501
'''
3가지 선택 중에 한 가지 선택이 가능하다.
1.주식 하나를 산다.
2.원하는 만큼 가지고 있는 주식을 판다.
3.아무것도 안한다.
어떻게 해야 최대 이익을 얻을 수 있을 지 계산
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    # 각 날짜 별 주식의 가격 정보
    data = list(map(int,input().split()))
    # 가격이 저렴할 때 사서, 비쌀때 파는 것이 이득
    # 뒤에서부터 가격이 저렴해지는 시점을 찾아서, 그 이후에 가장 비싸지는 시점에 판매한다.
    # 설정해둔 최고 가격보다 비싸지는 시점까지 계속해서 구매, 
    # 최초로 높아진다면 해당 가격에서 여태 산거 전부 판매하고, 
    # 그 이후로 다시 설정해둔 금액을 갱신하며 금액이 낮아질때까지 판매 가격을 갱신한다.
    max_point = data[-1] # 가장 마지막 가격을 판매 가격으로 임시 지정
    buy = []
    benefit = 0 # 얻게되는 이득
    for i in range(len(data)-1,-1,-1):
        # 역순에서 금액이 올라간다 => 주가가 하락중이다. 판매가를 갱신한다.
        if data[i] >= max_point: 
            # 구매해둔 주식이 있다면 모두 판매한다.
            if len(buy) != 0:
                for b in buy:
                    benefit += (max_point - b)
            max_point = data[i]
            buy = [] # 초기화
        else: # 주가가 상승중이라면 구매한다
            buy.append(data[i])
    # 반복문 종료이후 남아있는 주식을 모두 최대가에 판매한다.
    for b in buy:
        benefit += (max_point - b)
    print(benefit)
    