# https://www.acmicpc.net/problem/15655
'''
백트래킹 연습
'''
n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()  # 오름차순 출력을 위해

array = []  # 정답 배열


def backtracking(count, index):
    if count == m:  # m개의 숫자를 다 찾으면 출력 후 탈출
        print(*array)
        return

    # 중복을 방지해야함
    # => 자신의 인덱스보다 뒤에 있는 수는 고려하지 않으면 됨
    for i in range(index+1, n):
        array.append(numbers[i])
        backtracking(count+1, i)
        array.pop()


backtracking(0, -1)
