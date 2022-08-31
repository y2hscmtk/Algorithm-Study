# 다이나믹 프로그래밍

# 효율적인 화폐구성

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

# 우선 모든 금액에 대하여 만들수 없다고 가정, 1원짜리가 입력될 가능성이 존재하므로 10001원을 만들수 없다는 의미로 사용한다.
d = [10001] * (m+1)

d[0] = 0

for i in range(n):  # 화폐의 종류만큼 반복
    for j in range(array[i], m+1):  # 화폐의 금액에서부터,입력받은 금액 M전까지 반복
        if d[j-array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재할 경우
            d[j] = min(d[j], d[j-array[j]]+1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])
