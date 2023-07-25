# https://www.acmicpc.net/problem/15654
'''
백 트래킹 이용
'''

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()  # 작은 수 부터 출력되어야 하므로

used = [False for _ in range(n)]

array = []


def backtracking(count):
    global array, used
    if count == m:
        print(*array)

    for i in range(n):
        if not used[i]:
            array.append(numbers[i])
            used[i] = True
            backtracking(count+1)
            used[i] = False
            array.pop()


backtracking(0)

'''
다른 풀이

from itertools import permutations # 중복 허용

n,m = map(int,input().split())

numbers = list(map(int,input().split()))

numbers.sort()

for array in permutations(numbers,m):
    print(*array)
'''
