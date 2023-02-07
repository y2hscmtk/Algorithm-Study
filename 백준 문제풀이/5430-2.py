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
    data = input()
    # 데이터 분할
    data = data.replace('[', ',').replace(']', ',')
    # ,를 기준으로 단어 나누기
    data = data.split(',')
    # 에러 없이 명령이 수행됐는지 확인하기 위해서
    error = False
    # 알고리즘 수행
    for command in commands:
        # 뒤집기 명령
        if command == 'R':
            data.reverse()
        # 첫번째 단어 제거 명령
        elif command == 'D':
            # 제거할 단어가 없다면 error출력하고 다음 명령 입력받기
            if data[1] == '':
                print('error')
            # if len(data) == 2:
            #     print('error')
                error = True  # 에러발생 처리
                break
            else:
                # 제거할 단어가 남아있다면 제거
                del data[1]

    # 에러가 있었다면 결과출력없이 다음 테스트케이스로 넘어가기
    if error:
        continue
    # 단어 출력하기
    print('[', end='')
    for j in range(1, len(data)-1):
        if j == len(data)-2:
            print(data[j], end='')
        else:
            print(data[j], end=',')
    print(']')
