# https://www.acmicpc.net/problem/18113

'''
이분탐색
N,K,M = 전체 김밥수,꼬다리 길이,만들어야할 김밥조각의 개수

꼬다리를 잘라낼때
1. 2K보다 길다면, 양쪽을 모두 자른다.
2. K보다 길고, 2K보다 짧다면, 한쪽만 자른다.
3. 김밥길이가 K이거나, 그보다 짧다면 폐기한다.

꼬다리가 잘린 김밥을 '손질된 김밥'이라고 한다.
손질된 김밥은 모두 일정한 길이 P로 잘라서 최소 M개의 김밥을 만들고 싶다.
P를 최대한 길게 하는 것이 목표일때, P는 얼마로 해야하는가

만족하는 P가 없을 경우, -1을 출력한다.
'''
import sys
from bisect import *
N,K,M = map(int,input().split())
input = sys.stdin.readline

# 일단 K를 빼고 입력 받음 => K보다 작은 경우는 음수가 될것
data = [int(input())-K for _ in range(N)]
data.sort() # 이분탐색을 위해 정렬

# 탐색 진행
# K보다 큰지 검사해서, K보다 크다면 K를 뺀다.(양쪽 꼬다리 손질을 위해)
low,high = 0,data[-1]

# 만약 High가 음수라면 => 모든 꼬다리를 손질 할 수 없었다는 의미 => 종료
if high<=0:
    print(-1)
    sys.exit(0)

p = -1
while low<high:
    mid = (low+high)//2 # 중간값 설정
    if mid==0:
        break
    # mid로 몇개의 김밥조각을 나눌 수 있는지 확인
    count = 0
    for i in range(len(data)):
        if data[i] < 0: # 음수라면 고려 대상이 아님
            continue
        elif data[i] >= K: # 한쪽 더 손질가능하다면 손질
            # 손질한 김밥조각으로 나누기 수행
            count += (data[i]-K)//mid # mid로 몇개를 나눌 수 있는지 카운팅
        else: # 그냥 한쪽만 자른 경우
            count += data[i]//mid # 몇개의 김밥조각이 생기는지 카운팅
    # p가 mid일때 조건을 만족하는지 확인
    # 만약 count의 개수가 M개 미만이라면 => 너무 크게 잘랐다는 의미
    if count < M:
        # 너무 크게 잘랐으므로, 왼쪽 영역에서 탐색을 이어서 수행해야함
        high = mid
        # 조건을 만족하지 못했음으로, p값을 갱신하지 않음
    else: # count>=M인 경우 => 더 크게 자를수 있는지 확인 필요 => 우리는 큰 P가 목표이므로
        low = mid + 1
        p = max(p,mid) # 현재 mid는 조건을 만족하므로 갱신 가능함

print(p)


