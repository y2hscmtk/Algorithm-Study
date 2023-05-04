# https://www.acmicpc.net/problem/6603
from itertools import combinations

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    else:
        data = data[1:]
        data.sort()
        for select in combinations(data, 6):
            print(* list(select))
    print("")
