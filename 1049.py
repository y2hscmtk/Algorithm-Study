n, m = map(int, input().split())

six_set = []  # 6개들이를 살때의 가격
one_set = []  # 1개들이를 살때의 가격
min_price = 0  # 가격의 최소값

for i in range(m):
    data1, data2 = map(int, input().split())
    six_set.append(data1)
    one_set.appned(data2)

six_set.sort()  # 오름차순 정렬
one_set.sort()  # 내림차순 정렬
