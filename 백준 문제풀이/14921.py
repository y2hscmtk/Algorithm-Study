# https://www.acmicpc.net/problem/14921
n = int(input())
water = list(map(int,input().split()))
# 이분탐색을 위해 정렬
water.sort()

result = 200000001 # 가장 최악의 경우 + 1
s,e = 0,n-1
# 투 포인터를 이용하여 이분탐색 수행
while s<e:
    # 양 끝의 용액을 섞어서 절대값 확인
    temp = water[s] + water[e]
    
    # 더 값이 작아진다면
    if abs(temp) < abs(result):
        # 최소값 갱신
        result = temp
        if temp == 0:
            break # 정답 찾았음
    # 도 용액을 더한 값이 음수라면
    # 목표 => 0에 가깝게 만드는 것
    if temp<0: # 음수라면 음의 농도를 줄여야한다. => 양수에 가깝게 만들기 위해
        s+=1
    else: # 양수라면 양의 용액을 더 줄여봐도 괜찮다. => 0에 가깝게 만들기 위해
        e-=1 
print(result)