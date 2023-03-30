# https://www.acmicpc.net/problem/5555
'''
입력은 총 2 + N 줄 이다.

첫 번째 줄에는 1 자 이상 10 자 이하의 대문자로 구성된 찾고자 하는 문자열이 적혀있다.

두 번째 줄에는 반지의 개수 N (1 ≦ N ≦ 100)이 적혀있다.

2+i 줄(1 ≦ i ≦ N)엔 i개의 반지에 새겨져있고, 10 문자로 이루어진 문자열이 적혀있다.
'''
target = input()
n = int(input())
count = 0
for i in range(n):
    array = input()
    # 반지의 형태로 생각했을때, 처음과 끝이 이어지므로
    # 문자열을 2배 해준다면, 인덱스와 상관없이 문제해결 가능
    if target in array*2:
        count += 1

print(count)
