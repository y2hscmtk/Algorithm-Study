# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.

# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 아이디어 : 주어진 조건중 가장 가치가 큰 단위를 가장 많이 사용하면 된다.

n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))  # n 종류의 동전 오름차순으로 입력받기

coin.sort(reverse=True)  # 역순으로 사용하기 위해 내림차순으로 변환시킨다.

count = 0  # 사용한 동전의 개수를 표현하기 위한 변수

# print(k//coin[1])

for i in coin:
    count += k//i  # i
    k %= i

print(count)
