s = int(input())

n = 0
sum = 0

while True:
    n += 1
    sum += n
    if sum > s:
        break

print(n-1)
