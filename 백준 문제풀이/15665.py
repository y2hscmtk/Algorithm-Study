# https://www.acmicpc.net/problem/15665
'''
백 트래킹 활용
set()자료형을 이용하여 중복을 방지
'''
n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()  # 사전순으로 증가하여 출력해야함

result = []  # 정답을 저장하기 위함


def backtracking(count, array):
    if count == m:
        result.append(array)  # 생성한 숫자 set에 삽입
        return

    for i in range(n):
        array.append(numbers[i])
        backtracking(count+1, array)
        array.pop()


backtracking(0, [])  # 백트래킹으로 숫자 배열 생성

# 정답 출력
for array in result:
    print(*array)
