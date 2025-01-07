import heapq
n = int(input())
x = [] # 최소힙으로 사용

# Write your code here!
for _ in range(n):
    num = int(input()) # 입력값
    # 1.입력이 0이라면 가장 작은 값을 출력하고 그 값을 배열에서 제거한다.
    # 배열이 비어잇는 상태라면 0을 출력한다.
    if num == 0:
        if len(x) == 0:
            print(0)
        else:
            print(heapq.heappop(x))
    else:
        heapq.heappush(x,num) # 지연수라면 배열에 삽입