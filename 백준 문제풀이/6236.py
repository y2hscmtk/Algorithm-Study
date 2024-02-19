'''
인출 금액 K를 최소화
K를 0~MAX 사이를 돌면서 매개변수 탐색 수행 => Middle원
Middle원을 인출하였을때, 조건을 만족할 수 있는지 확인 후, 최소한의 금액으로 만족 가능할때까지 이분탐색
(정확히 M번만 돈을 인출한다. 정확히  M번 인출해서 돈을 다 담을 수있는지 확인한다.)
(돈이 부족하면 남은 금액은 통장에 넣고 다시 K원 인출 -> 돈이 부족하면 인출횟수 증가시키고 K원으로 다시 시작)
'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

day = [] # 해당 날짜에 얼만큼의 돈을 소비하는지
for _ in range(N):
    day.append(int(input()))
    
start,end = max(day),sum(day)
result = end
    
def count_num(money): # money : 하루에 쓸 수 있는 돈
    now = money
    count = 1 # 인출 횟수
    for spend in day: # 당일 소비액
        if now < spend:
            now = money
            count += 1 # 인출 +1
        now -= spend
    return count
        
while start<=end:
    mid = (start + end)//2
    # mid원을 하루 인출 금액으로 설정시, 몇번의 인출로 해결되는지 확인
    count = count_num(mid)
    # M번의 인출보다 같거나 적은 횟수만큼 인출한다. -> 인출 선정 금액이 너무 크다 -> 줄여야한다.
    if count<=M:
        end = mid-1 # 범위를 왼쪽으로
        result = min(result,mid) # 갱신
    else: # 횟수가 더 많다. -> 줄여야한다.
        start = mid+1
print(result)