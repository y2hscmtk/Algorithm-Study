# 백준 13305번

# https://www.acmicpc.net/problem/13305


# 아이디어 : 처음 도시부터 다음도시까지의 거리만큼 기름을 구매한 후, 다음 도시로 이동,
#           다음 도시에서 또 다른 도시까지 거리만큼 두번째 도시에서 기름을 구매한후의 가격과, 이전도시에서 기름을 구매했을때의 가격을 비교하여
#           더 작은쪽의 값을 채택한다. # 마지막 도시에서는 기름을 구매할수 없으므로 고려할필요없다.

n = int(input())  # 도시의 개수

d = list(map(int, input().split()))  # 도시간에 서로 떨어진 km수를 저장할 배열

city_oil = list(map(int, input().split()))  # 각 도시의 기름 값을 저장할 배열

price = city_oil[0]
sum = 0
# 최소 기름값 탐색 시작
for i in range(n-1):  # 마지막 도시는 고려할 대상이 아니므로 n-1번 비교
    if price > city_oil[i]:
        price = city_oil[i]
    sum += (price*d[i])

print(sum)
