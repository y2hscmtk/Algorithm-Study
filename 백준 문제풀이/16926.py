# https://www.acmicpc.net/problem/16926
'''
배열 돌리기
배열은 반시계방향으로 돌린다.
nxm 배열을 r번 회전시킨 결과를 출력하라.
'''
n, m, r = map(int, input().split())
array = list(map(int, input().split()) for _ in range(n))


def turn():
    for _ in range(n//2):
        temp = array[0][0]
        # for i in range(m):
