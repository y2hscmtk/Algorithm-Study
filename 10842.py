from collections import deque

import sys

input = sys.stdin.readline

# 명령의 횟수

n = int(input())

count = 0

for i in range(n):

    queue = deque()

    # 명령 입력받기

    command = list(map(str, input().split()))

    # push 명령이 존재한다면 숫자와 분할

    if command[0] == "push":

        queue.append(int(command[1]))

        count += 1  # 큐에 내용물 추가

    elif command[0] == "front":

        # 큐가 비어있다면 -1 출력

        if count == 0:

            print(-1)

        else:

            # 가장 앞에 있는 정수 출력

            print(queue.popleft())

    elif command[0] == "size":

        # 큐의 크기를 출력한다.

        print(count)

    elif command[0] == "empty":

        # 큐가 비어있으면 1을 출력하고 아니면 0을 출력한다.

        if count == 0:

            print(1)

        else:

            print(0)

    elif command[0] == "pop":

        # 큐가 비어있다면

        if count == 0:

            print(-1)

        else:  # 큐가 비어있지 않다면

            print(queue.popleft())

            count -= 1

    elif command[0] == "back":

               # 큐가 비어있다면

         if count == 0:

             print(-1)

         else:  # 큐가 비어있지 않다면

             print(queue.pop())

             count -= 1

