n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 오름차순 정렬
b.sort(reverse=True)  # 내림차순 정렬

s = 0

for i in range(n):
    s += a[i]*b[i]

print(s)
