# https://www.acmicpc.net/problem/12018

# 목표 : 최대한 많은 과목을 듣는것
# 수강권을 얻는 방법 => 많이 투자한 순에서 해당 과목의 수강신청 인원만큼 받아줌
# => 가장 적절한 값으로 수강에 성공하는 것이 중요
# 
# 아이디어 : 다른 사람들이 입력한 가격을 내림차순으로 정렬
# 정렬한 가격들 중에서, 수강신청 인원의 마지막에 들어가는 것이 가장 적절한 가격
# 가장 이득을 보는 가격을 과목 가격 배열에 삽입
# 과목 가격 배열을 오름차순으로 정렬하고 앞에서부터 차례로 포인트가 만족하는한 과목을 담으면 된다.

import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # 과목 수, 보유중인 마일리지 양

subject_price = [1]*n

for i in range(n):
    p,l = map(int,input().split()) # 신청한 사람 수,과목의 수강 인원
    data = list(map(int,input().split()))
    # 수강 가능 인원이 신청자 보다 많을 경우 => 1원만 입력해도 입찰이 가능
    if p<l:
        continue # 넘어감 => 1원
    data.sort(reverse=True) # 내림차순 정렬 => 위에서부터 컷
    # 적정 가격은 l-1번째 사람이 입찰한가격과 같은 값(같은 값이면 우선순위가 높으므로)
    subject_price[i] = data[l-1]

# 몇과목을 수강할 수 있는지 계산
count = 0 # 들을 수 있는 가격의 수
subject_price.sort()
for price in subject_price:
    if m-price >= 0: # 현재 마일리지에서 수강 가능하면
        count+=1 # 수강가능
        m-=price # 수강하기
    else:
        break # 더이상 못듣는다면 탐색 종료
print(count)