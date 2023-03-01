# https://www.acmicpc.net/problem/10819

'''
문제
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.
'''
from itertools import permutations

n = int(input())

numbers = list(map(int, input().split()))

result = -800  # 최솟값이 될수 있는 경우

# 기존의 숫자 배열을 순열을 이용하여 순서있게 재배치
for array in permutations(numbers, n):
    array_sum = 0  # 새로운 수열을 정해진 식에 따라 계산하여 저장할 변수
    for i in range(n):
        array_sum += abs(array[i] - array[i+1])
        # 계산식의 조건에따라 i가 n-2가 될때까지만 식을 계산한다.
        if i == n-2:
            break
    # 계산이 끝난 뒤, 최댓값을 갱신한다.
    result = max(result, array_sum)

print(result)
