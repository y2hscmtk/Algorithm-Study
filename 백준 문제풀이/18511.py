# https://www.acmicpc.net/problem/18511
'''
N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오. 

K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.

예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다
'''
N, S = map(int, input().split())
K = list(input().split())
size = len(str(N))
result = 0

# N보다 작거나 같은 자연수 중에서 집합 K의 원소로만 구성된 가장 큰 수 찾기
def recursion(depth, curr):
    global result
    if curr:
        num = int(curr)
        # 현재 설정된 수가 N보다 작거나 같은지 파악하고 갱신
        if num <= N:
            result = max(result, num)
    # 재귀 함수 종료 조건: 자리 수가 size를 넘지 않도록 설정
    if depth == size:
        return
    for n in K:
        recursion(depth+1, curr+n)

recursion(0, '')
print(result)