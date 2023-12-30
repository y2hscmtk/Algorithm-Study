# https://www.acmicpc.net/problem/13908
from itertools import product  # 중복 순열
'''
중복 순열을 이용하여 만들 수 있는 모든 숫자를 만들어보고
만들어진 숫자가 '이미 알고 있는 수'를 포함한다면 result +=1
'''
result = 0
numbers = [i for i in range(10)]
n, m = map(int, input().split())
if m == 0:
    known = []
else:
    known = list(map(int, input().split()))  # 이미 알고 있는 수

for number_array in product(numbers, repeat=n):  # n개의 수 뽑기
    # 만들어진 수가 known을 모두 포함하는지 확인
    error = False
    for number in known:
        # 뽑은 숫자 배열에 known의 모든 수가 포함되어 있는지 확인
        if number not in number_array:  # 포함되어 있지 않다면
            error = True
            break
    if not error:  # 문제없이 known의 모든 수를 포함하였다면
        result += 1


print(result)
