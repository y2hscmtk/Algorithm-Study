import heapq
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

pq = []

# 1. 입력으로 주어진 각 점들과 원점에서의 거리를 먼저 삽입
for x,y in points:
    diff = abs(x) + abs(y)
    heapq.heappush(pq,(diff,x,y)) # diff,x,y 순의 우선순위

# 2. 최단거리가 가까운 순으로 연산 수행
for _ in range(m):
    diff,x,y = heapq.heappop(pq)
    nx,ny = x + 2, y + 2
    new_diff = abs(nx) + abs(ny)
    heapq.heappush(pq,(new_diff,nx,ny))

# 3. m번 수행한 후 원점에서 가장 가까운 점 출력
_,x,y = heapq.heappop(pq)
print(x,y)
