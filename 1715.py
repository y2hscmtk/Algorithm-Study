# 백준 1715번

# 아이디어 : 우선순위 큐와 허프만 코드 생성과정을 이용한다.
from heapq import heappush, heappop
n = int(input())

# 삽입하는 방식 => 최소 힙의 방식으로 삽입
heap = []

# 문자를 입력받고, 최소 힙에 삽입한다.
# 먼저 문자를 최소힙의 말단에 삽입하고,부모노드와 비교하며 위치를 조정한다.

for _ in range(n):
    heappush(heap, int(input()))  # 사용자로부터 수를 입력받아 힙에 푸쉬

count = 0

while heap:  # 힙이 존재하는 동안
    e1 = heappop(heap)
    e2 = heappop(heap)
    item = e1 + e2
    count += item
    if len(heap) == 0:
        break  # 힙이 비워져있다면 모든 반복을 마쳤다는 뜻
    heappush(heap, item)


print(count)
