# https://www.acmicpc.net/problem/14235
'''
아이들과 거점지 방문 횟수 N
N개의 줄에는 0 또는 배열
배열인 경우 -> 선물 충전
0일 경우 -> 배열에서 가장 최대값 반환 -> 우선순위 큐 사용하면 시간 단축될듯

풀이참조여부 : x
'''
import heapq

hq = [] # 우선순위 큐로 사용

for _ in range(int(input())):
    a = list(map(int,input().split()))
    # 값이 하나뿐이며, 그 값이 0일 경우
    if len(a) == 1 and a[0] == 0:
        if hq: # 선물 존재시 
            # 최대 가치를 지닌 선물 추출
            present = heapq.heappop(hq)
            print(abs(present))
        else:
            print(-1) # 선물이 없다면 -1 출력
    else:
        for i in range(1,len(a)):
            heapq.heappush(hq,-a[i])