# https://www.acmicpc.net/problem/2075
import heapq
import sys
input = sys.stdin.readline
n = int(input())

# 최대힙에 들어갈 숫자의 개수를 n개로 제한하여 문제를 해결한다
# => 메모리 초과 방지
# 한줄씩 입력받으면서 최대힙의 개수가 n개를 초과하지 않도록하고,
# 만약 초과하게 된다면, 기존의 최대값과 비교하여 최대힙의 값을 업데이트한다.
heap = [] # 최대 힙으로 사용하기 위한 배열
# 최소 힙을 최대힙으로 변형해서 사용하기 위한 트릭으로, -로 삽입한다.
for i in range(n):
    array = list(map(int,input().split()))
    for num in array:
        # 만약 최대힙의 사이즈가 n을 초과하지 않는다면
        if len(heap) < n:
            heapq.heappush(heap,num) # 숫자를 삽입한다.
        else: # 만약 초과하게 되었다면, r가장 작은 숫자를 팝하여 확인
            temp = heapq.heappop(heap)
            if temp < num:
                heapq.heappush(heap,num) # 삽입
            else: # 기존 최대힙의 값이 더 크다면
                heapq.heappush(heap,temp) # 기존값 다시 삽입
                
print(heap[0])
