n, m = map(int, input().split())
number = [i for i in range(1, n+1)]
for i in range(m):
    a, b = map(int, input().split())
    number[a-1], number[b-1] = number[b-1], number[a-1]

print(*number)
