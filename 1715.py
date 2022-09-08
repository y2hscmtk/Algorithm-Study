n = int(input())

card = []

for i in range(n):
    card.append(int(input()))

card.sort()  # 오름차순 변경

sum = 0

for i in range(n):
    for j in range(0, i+1):
        sum += card[j]

sum - card[0]

print(sum)
