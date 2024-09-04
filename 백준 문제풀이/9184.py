# https://www.acmicpc.net/problem/9184
'''
재귀 + 다이나믹
메모이제이션 기법을 이용하여 a,b,c 경우에 대해 각각 기록
-50 ≤ a, b, c ≤ 50
'''
memo = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]

# -50 ~ 0 까지의 모든 수는 모두 1로 기록
for i in range(51):
    for j in range(51):
        for k in range(51):
            memo[i][j][k] = 1

def w(a,b,c):
    # 이미 메모해둔 과가 있다면 출력 후 종료
    if memo[a+50][b+50][c+50] != -1:
        return memo[a+50][b+50][c+50]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        memo[a+50][b+50][c+50] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a+50][b+50][c+50]
    else:
        memo[a-1+50][b+50][c+50] = w(a-1, b, c) 
        memo[a-1+50][b-1+50][c+50] =  w(a-1, b-1, c)
        memo[a-1+50][b+50][c-1+50] = w(a-1, b, c-1)
        memo[a-1+50][b-1+50][c-1+50] = w(a-1, b-1, c-1)
        memo[a+50][b+50][c+50] = memo[a-1+50][b+50][c+50] + memo[a-1+50][b-1+50][c+50] + memo[a-1+50][b+50][c-1+50] - memo[a-1+50][b-1+50][c-1+50]
        return memo[a+50][b+50][c+50]

while True:
    a,b,c = map(int,input().split())
    if (a,b,c) == (-1,-1,-1):
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

