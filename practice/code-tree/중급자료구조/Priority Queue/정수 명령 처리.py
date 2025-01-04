# 정수 명령 처리 6
import heapq

arr = []
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "push":
        heapq.heappush(arr,-int(cmd[1]))
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "empty":
        print([0,1][len(arr)==0]) # 비어있다면 1, 아니면 0 출력
    elif cmd[0] == "pop":
        print(-int(heapq.heappop(arr)))
    elif cmd[0] == "top":
        print(-arr[0])