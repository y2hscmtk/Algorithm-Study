# https://www.acmicpc.net/problem/11576
'''
A진법으로 나타낸 숫자를 B진법으로 변환시켜주는 프로그램을 작성
A와 B는 모두 2이상 30이하의 자연수다.
입력으로 주어진 A진법으로 나타낸 수를 B진법으로 변환하여 출력한다.
'''
# a진법을 b진법으로 변환
a, b = map(int, input().split())
# A진법으로 나타낸 숫자의 자리수의 개수 m
m = int(input())
# m개의 수
array = list(map(int, input().split()))
array.reverse()

# a진법 수를 10진법로 변환하기
# 0000 => 0*a^3 + 0*a^2 + 0*a^1 + 0*a^0


ten = 0  # 10진법으로 변환하기 위해
# 먼저 문자를 10진법으로 변경하고, 10진법에서 다시 b진법으로 변경하여 출력
for i in range(m):
    ten += array[i]*(a**i)

result = []
while ten:
    result.append(str(ten % b))  # 나머지를 삽입 => 나머지를 거꾸로 읽으면 변환
    ten //= b

result.reverse()
print(' '.join(result))
