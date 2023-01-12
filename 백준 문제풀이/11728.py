# https://www.acmicpc.net/problem/11728

'''
두 배열을 합친후 정렬하여 한줄에 공백으로 구분하여 출력하는 프로그램
'''

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = a + b  # 두 배열을 합한다.

c.sort()  # 정렬하고

for data in c:
    print(data, end=' ')  # 공백으로 구분하여 한줄에 출력한다.
