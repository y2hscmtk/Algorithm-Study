# https://www.acmicpc.net/problem/1966

'''
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’,
즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다.
하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
'''

from collections import deque

t = int(input())  # 테스트케이스의 횟수

# 큐를 사용하기 위해 deque를 이용
queue = deque()

num = 0

for _ in range(t):  # t번의 시행을 반복
    queue.clear()  # 큐 비우기
    # 공백을 기준으로 입력받을 데이터의 개수와, 인쇄 순번이 궁금한 문서의 인덱스 번호를 입력받는다.
    size, index = map(int, input().split())  # 인덱스 번호가 핵심
    # size개의 데이터를 입력받는다.
    data_list = list(map(int, input().split()))
    # 큐로 옮긴다.
    for i in range(size):
        queue.append([data_list[i], i])  # 인덱스번호와 함께 데이터를 삽입

    final_data = []

    # 여기서 부터 비교 시작
    while queue:
        check = False
        target = queue.popleft()  # 큐의 성질을 이용하기 위해
        # 타겟과 나머지 데이터들의 우선순위를 비교해야함
        # 나머지 데이터들이 깨지면 안되므로 복사 필요
        queue_copy = queue.copy()
        # if len(queue_copy) == 0:
        #     final_data.append(target)
        for i in range(len(queue_copy)):
            c = queue_copy.popleft()
            if target[0] < c[0]:  # 데이터끼리 비교한다.
                queue.append(target)  # 타겟을 맨 뒤로 이동
                check = True
                break  # 하나라도 높은것을 확인했다면 더이상 반복하지 않는다.
        # 반복문에서 더 높은 수를 발견하지 못했다면
        if not check:
            final_data.append(target)  # 삽입
    # 해당하는 인덱스를 출력하기 위함
    for i in range(len(final_data)):
        if final_data[i][1] == index:  # 해당하는 인덱스 발견시
            print(i+1)  # 프린트 되는 순번을 출력
            break
