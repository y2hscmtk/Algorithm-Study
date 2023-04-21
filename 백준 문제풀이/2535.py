# https://www.acmicpc.net/problem/2535
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 성적을 기준으로 오름차순 정렬
data.sort(reverse=True, key=lambda x: x[2])

country = []
result = []
check = 0
for c, n, p in data:
    if check == 3:
        break  # 3명 선발시 종료
    if country.count(c) < 2:
        result.append([c, n])
        country.append(c)
        check += 1  # 한명 선발

for c, n in result:
    print(c, n)
