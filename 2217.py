n = int(input())

data = []

for i in range(n):
    data.append(int(input()))

data.sort()  # 오름차순 정렬

w = 0

for i in range(n):
    if w <= (data[i]*(n-i)):
        w = data[i]*(n-i)

print(w)
