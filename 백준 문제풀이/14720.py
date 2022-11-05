# 우유 마시기

n = int(input())

data = list(map(int, input().split()))

count = 0
for i in range(n):
    if i == 0:
        if data[i] == 0:
            count += 1  # 맨 처음에는 딸기우유를 한 팩 마신다
    else:

        if data[i] == 1 and data[i-1] == 0:  # 초코우유 집에 방문했을 때,이전에 딸기우유을 마셨다면
            count += 1  # 초코우유를 한 팩 마신다.
        if i >= 2:
            if data[i] == 2 and data[i-1] == 1 and data[i-2] == 0:
                count += 1
            elif data[i] == 0 and data[i-1] == 2 and data[i-2] == 1:
                count += 1  # 맨 처음에는 딸기우유를 한 팩 마신다

print(count)
