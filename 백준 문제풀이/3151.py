# https://www.acmicpc.net/problem/3151
'''
먼저 전체 데이터를 정렬
왼쪽에서 부터 수를 하나 지정, 해당 수와 더해서 0이 되도록하는 조건수 지정
해당 수의 오른쪽 수에서 부터 투포인터를 사용하여 투포인터를 통해 조건 수를 만들 수 있는지 확인
조건수를 만들 수 있는 경우가 많을 수 있으므로 항상 끝과 끝을 탐색해야함
'''
import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0 # 경우의 수(정답에 해당)
# 조건수 지정
for i in range(N-2):
    # i번째 수와 더해서 0이 될 수 있는 조건 수 지정
    target = -data[i]
    start,end = i+1,N-1 # 이분탐색의 양 끝점 지점(투 포인터 지정)
    while start<end:
        temp = data[start] + data[end]
        # 양 끝점을 더한 수가
        if temp == target:
            # 값이 같은 경우
            if data[start] == data[end]:
                result += (end-start)
            else: # 값이 다를 경우
                # 오른쪽에 해당하는 값의 개수만큼
                index = bisect_left(data,data[end]) # data[end]중 가장 왼쪽 인덱스 리턴
                result += end-index+1
            start+=1
        elif temp < target: 
            start+=1
        else: # temp > target
            end-=1

print(result)