# 배열에서 특정 원소의 개수가 몇개인지 출력하는 프로그램

from bisect import bisect_left, bisect_right

# n과 x 입력받기
n, x = map(int, input().split())

# 공백으로 구분하여 정수 리스트 array 입력받기
array = list(map(int, input().split()))

result = 0
