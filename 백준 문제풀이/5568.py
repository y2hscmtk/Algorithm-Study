# https://www.acmicpc.net/problem/5568
'''
순서가 중요하므로, 순열 이용
만든 숫자는 set자료형에 넣어서 중복 방지
정답은 set의 크기
'''
from itertools import permutations

n = int(input())
k = int(input())

# 합치기 용이하게 글자로 입력받기
numbers = [input() for _ in range(n)]

new_num = set()

# numbers에서 k개를 뽑는 경우의 수 나열
for select in permutations(numbers, k):
    new_num.add(''.join(select))

print(len(new_num))
