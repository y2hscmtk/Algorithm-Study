# 백준 2751번

# 레코드의 최대 개수가 매우 많으므로 히프정렬, 퀵 정렬 등의 정렬 알고리즘을 사용해야 시간초과 판정을 벗어날수 있다.
# 또한 입출력 시간을 줄이기 위해 sys를 import해야한다.

import sys
import heapq

# def heapsort(iterable):
#     heap = []
#     result = []
#     for value in iterable:
#         heapq.heappush(heap, value)
#     for i in range(len(heap)):
#         result.append(heapq.heappop(heap))
#     return result

n = int(input())  # n개의 자료를 입력받을것

heap = []
# sorted_list = []

# 히프에 입력받은 데이터를 삽입하고,
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

# 정렬된 히프에서 하나씩 뽑아서 출력한다. => 히프에 삽입하는 순간 이미 정렬이 완료되므로
for i in range(len(heap)):
    print(heapq.heappop(heap))

# for i in li:
#     print(i)
