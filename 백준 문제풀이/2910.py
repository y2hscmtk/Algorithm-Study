n, c = map(int, input().split())

number = list(map(int, input().split()))

dict = {}

# 숫자 빈도 기록
for num in number:
    if num not in dict:
        dict[num] = 1
    else:
        dict[num] += 1
result = []
for v in dict:
    result.append([v, dict[v]])
result.sort(key=lambda x: -x[1])

for num, count in result:
    for _ in range(count):
        print(num, end=' ')
