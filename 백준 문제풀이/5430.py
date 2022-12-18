# https://www.acmicpc.net/problem/5430

'''
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. 

AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 

배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다.

예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
'''

from collections import deque
# 덱을 이용

t = int(input())

queue = deque()

for _ in range(t):
    queue.clear()  # 배열 비우기
    error = False  # 에러가 발생했는지 여부를 기록하기 위함
    command = input()  # 어떤 명령을 수행할것인지 입력받음
    # R은 배열 뒤집기, D는 처음 두 수를 버림
    size = int(input())  # 입력받을 숫자의 개수
    # 배열 입력받기
    input_data = input()  # 배열을 입력받아 저장
    # 콤마를 기준으로 배열 나누기
    # 구분자가 여러개있을때는 구분자를 다른 문자로 바꾼다
    input_data = input_data.replace('[', ',').replace(']', ',')

    for i in range(len(input_data)):
        if input_data[i] == ',':
            continue
        else:  # ,가 아닌 숫자를 큐에 저장한다.
            queue.append(int(input_data[i]))

    # 명령을 수행 R은 뒤집기, D는 앞에서부터 데이터를 삭제
    # 단 배열이 비어있을때는 error 출력
    for i in range(len(command)):
        if command[i] == 'R':
            queue.reverse()  # 배열 뒤집기
        elif command[i] == 'D':
            if len(queue) == 0:  # 입력받은 데이터가 없다면
                print("error")
                error = True  # 에러사실 기록
            else:
                queue.popleft()  # 왼쪽에서 부터 데이터 제거

    print_data = list(queue)  # 리스트 형태로 변환
    if not error:
        print(print_data)  # 오류가 없다면 결과 출력
    # # # 에러가 나지 않았다면 결과 데이터 출력
    # # if not error:
    # #     print("[")
    # #     for i in range(len(queue)):
    # #         num = queue.pop()
    # #         print(num)
    # #         if len(queue) != 1:  # 마지막 수가 아니라면
    # #             print(",")
    #     print("]")
