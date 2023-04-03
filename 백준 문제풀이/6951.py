# https://www.acmicpc.net/problem/6591
# n개의 원소 중에서 k개를 순서 없이 선택하는 방법의 수는 몇 가지 일까?

# 순서 없이 선택하는 방법 => 조합
# nCr = n!/r!(n-r)!

# 순서 있이 선택하는 방법 => 순열
# nPk = n!/(n-k)!
# from math import factorial

# # nCr = nC(n-r) 임을 이용해야 시간초과 판정을 피할수있음
# def nCr(n, r):
#     return factorial(n)//(factorial(r)*factorial(n-r))


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        # nCr 계산
        n, r = 1, 1
        # 4C2 => 4*3/2*1
        # a=4 b=2 a-b =2

        # a의 절반보다 b숫자가 크다면
        # b를 a-b한값으로 바꿔줘야함
        # 더 많은 계산을 피하기 위해
        if b > a//2:
            b = a-b

        for i in range(a, a-b, -1):
            n *= i
        for i in range(b, 1, -1):
            r *= i
        print(n//r)
