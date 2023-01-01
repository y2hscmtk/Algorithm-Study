# https://www.acmicpc.net/problem/10866

'''
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.

pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.

front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
# 덱을 이용하기 위해 덱 import
from collections import deque

# 시간초과 판정을 피하기 위해
import sys
input = sys.stdin.readline


n = int(input())

# 덱 생성
deq = deque()

for _ in range(n):
    # 명령 입력받기
    command = list(map(str, input().split()))

    if "push" in command[0]:
        # 푸시 명령에 한하여 command[1]이 존재함
        x = command[1]
        # push back인지 push front인지에 따라 다른 명령 수행
        if command[0] == "push_front":
            # push_front 명령은 정수 x를 덱의 앞에 넣는다.
            deq.appendleft(x)
        elif command[0] == "push_back":
            # push_back 명령은 정수 x를 덱의 뒤에 넣는다.
            deq.append(x)
    elif command[0] == "pop_front":
        # 덱에 정수가 없는 경우에는 -1을 출력한다.
        if len(deq) == 0:
            print(-1)
        else:
            # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.
            print(deq.popleft())
    elif command[0] == "pop_back":
        # 덱에 정수가 없는 경우에는 -1을 출력한다.
        if len(deq) == 0:
            print(-1)
        else:
            # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
            print(deq.pop())
    # 덱에 들어있는 정수의 개수를 출력한다.
    elif command[0] == "size":
        print(len(deq))
    # 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif command[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(deq) == 0:
            print(-1)
        else:
            # 덱의 가장 앞에 있는 정수를 출력한다.
            item = deq.popleft()
            deq.appendleft(item)
            print(item)
    elif command[0] == "back":
        # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(deq) == 0:
            print(-1)
        else:
            # 덱의 가장 뒤에 있는 정수를 출력한다.
            item = deq.pop()
            deq.append(item)
            print(item)
