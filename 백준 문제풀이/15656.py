# https://www.acmicpc.net/problem/15656
'''
백트래킹 연습
'''
n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()  # 오름차순 출력을 위해

array = []  # 정답 배열


def backtracking(count):
    if count == m:  # m개의 숫자를 다 찾으면 출력 후 탈출
        print(*array)
        return

    for i in range(n):
        array.append(numbers[i])
        backtracking(count+1)
        array.pop()


backtracking(0)
