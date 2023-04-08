# https://www.acmicpc.net/problem/8974
# 미리 만들어두고 뽑기

# 한 줄에 양의 정수 A와 B가 주어진다. (1 ≤ A ≤ B ≤ 1000)

data = [0]
for i in range(1, 1001):
    for j in range(i):
        data.append(i)

a, b = map(int, input().split())
print(sum(data[a:b+1]))
