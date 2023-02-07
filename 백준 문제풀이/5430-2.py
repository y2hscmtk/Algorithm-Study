# https://www.acmicpc.net/problem/5430

'''
AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 
이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 
배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
함수는 조합해서 한 번에 사용할 수 있다. 
예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 
예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.
배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)
전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
'''
from collections import deque
# 테스트 케이스의 수
t = int(input())

for i in range(t):
    # 수행할 명령
    commands = list(input())
    # 입력받을 데이터의 수
    n = int(input())
    # 입력받을 데이터
    # 앞뒤의 []은 무시하고 데이터만 입력받음, strip을 이용하여 1이전(0)과 -1번째 값을 지움
    # 이후 ','을 기준으로 나누기
    data = deque(input().strip()[1:-1].split(','))

    # 단어의 개수가 0개일경우 비어있는 덱으로 전환
    if n == 0:
        data = deque()

    # 에러 없이 명령이 수행됐는지 확인하기 위해서
    error = False
    # 홀수번 reverse명령이 있을때만 뒤집기 명령을 수행하기 위함
    reverse = False

    # 명령 수행
    for command in commands:
        # 뒤집기 명령
        if command == 'R':
            # 기존 reverse명령이 True라면 False로, 아니면 True로 바꾼다.
            reverse = False if reverse else True
        # 첫번째 단어 제거 명령
        elif command == 'D':
            # 제거할 단어가 덱에 남아있는 상태일때만 명령 수행
            if data:
                # reverse명령이 있는 상태라면 오른쪽 끝 값을 제거해야함
                if reverse:
                    data.pop()
            # reverse명령이 없는 상태라면 왼쪽 끝 값을 제거해야함
                else:
                    data.popleft()
            # 제거할 단어가 없는상태라면 반복 종료후 error출력
            else:
                print('error')
                error = True  # 에러발생 확인
                break
    # 에러가 있었다면 결과출력없이 다음 테스트케이스로 넘어가기
    if error:
        continue
    # 최종적으로 reverse명령이 홀수번 있었는지 확인하여 배열 뒤집기
    if reverse:
        data.reverse()
    # 최종 결과 출력
    # data문자열 사이에 join을 이용하여 ,를 삽입 ','.join(리스트)
    print("["+",".join(data)+"]")
