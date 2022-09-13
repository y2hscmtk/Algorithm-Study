# https://www.acmicpc.net/problem/1049

n, m = map(int, input().split())

six_set = []  # 6개들이를 살때의 가격
one_set = []  # 1개들이를 살때의 가격
min_price = 0  # 가격의 최소값

for i in range(m):
    data1, data2 = map(int, input().split())
    six_set.append(data1)
    one_set.append(data2)

six_set.sort()  # 오름차순 정렬
one_set.sort()  # 내림차순 정렬

if n % 6 == 0:  # 6개의 배수개일때
    min_price = six_set[0]*n//6
else:
    min_price = six_set[0]*(n//6) + one_set[0]*(n % 6)
if six_set[0]*(n//6) + six_set[0] < min_price:
    min_price = six_set[0]*(n//6) + six_set[0]
if one_set[0]*n < min_price:
    min_price = one_set[0]*n


print(min_price)
