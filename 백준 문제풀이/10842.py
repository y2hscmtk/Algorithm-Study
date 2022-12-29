# https://www.acmicpc.net/problem/10845

'''
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from collections import deque

import sys

input = sys.stdin.readline

# 명령의 횟수
n = int(input())

# 명령을 저장할 큐 생성
queue = deque()


# 큐는 FIFO 알고리즘으로, 먼저 들어간것이 먼저 나오게 된다.
for i in range(n):

    # 명령 입력받기
    command = list(map(str, input().split()))
    # push 명령이 존재한다면 숫자와 분할
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "front":
        # 큐가 비어있지 않다면 연산 수행
        # 가장 앞에 있는 정수 출력
        # => 덱 자료구조에 peek이 구현되어 있지 않으므로
        if queue:
            item = queue.popleft()
            # 팝한 후에 다시 삽입해 줘야함
            queue.appendleft(item)
            print(item)
        # 비어있다면 -1출력
        else:
            print(-1)
    elif command[0] == "size":
        # 큐의 크기를 출력한다.
        print(len(queue))
    elif command[0] == "empty":
        # 큐가 비어있으면 1을 출력하고 아니면 0을 출력한다.
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == "pop":
        # 큐가 비어있지않다면 연산
        if queue:
            print(queue.popleft())
        else:  # 큐가 비어있지 않다면
            print(-1)
    elif command[0] == "back":
        # 큐가 비어있지 않다면 연산 수행
        if queue:
            item = queue.pop()
            queue.append(item)
            print(item)
        else:  # 큐가 비어있지 않다면
            # 팝을 하되, 큐에서 데이터가 제거되지 않도록 다시 삽입한다.
            print(-1)
