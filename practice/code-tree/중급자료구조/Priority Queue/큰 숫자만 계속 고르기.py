'''
n개의 숫자 중 가장 큰 숫자를 골라 1씩 빼는 작업을 m번 반복, 이후 남아있는 숫자들 중 최대값 구하기
'''
import heapq
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queue = []
# 초기 정수 삽입
for num in arr:
    heapq.heappush(queue,-num)

# m번 반복
for _ in range(m):
    num = -heapq.heappop(queue)
    # 1뺀 이후 다시 삽입
    heapq.heappush(queue,-(num-1))

# 남아있는 수 최대값 출력
print(-queue[0])