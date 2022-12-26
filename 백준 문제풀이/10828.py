# https://www.acmicpc.net/problem/10828


'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

'''
import sys

input = sys.stdin.readline

# 스택의 역할을 할 리스트 생성
stack = []

# 명령의 횟수
n = int(input())

# len 명령을 최대한 줄이기 위해 스택의 크기를 측정할 변수 생성
count = 0

for i in range(n):
    # 명령 입력받기
    command = list(map(str, input().split()))
    # push 명령이 존재한다면 숫자와 분할
    if command[0] == "push":
        stack.append(int(command[1]))
        count += 1  # 스택 내용물 추가
    elif command[0] == "top":
        # 스택이 비어있다면 -1 출력
        if count == 0:
            print(-1)
        else:
            # 가장 위에 있는 정수 출력
            print(stack[-1])
    elif command[0] == "size":
        # 스택의 크기를 출력한다.
        print(count)
    elif command[0] == "empty":
        # 스택이 비어있으면 1을 출력하고 아니면 0을 출력한다.
        if count == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "pop":
        # 스택이 비어있다면
        if count == 0:
            print(-1)
        else:  # 스택이 비어있지 않다면
            print(stack.pop())
            count -= 1
