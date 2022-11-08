# https://www.acmicpc.net/problem/2798

'''
아이디어1
다이나믹 프로그래밍 기법을 이용하여 풀면 될듯?
주어진 숫자들을 내림차순으로 정렬한 뒤, 숫자들을 뽑으면서 해당 숫자가 M을 넘지않는 수 중 최고의 수라면 뽑는다.
'''

n, m = map(int, input().split())

cards = list(map(int, input().split()))

cards.sort(reverse=True)  # 내림차순으로 정렬
check = False

for i in range(n):
    result, count = 0, 0
    for j in range(i, n):
        if result + cards[j] <= m:
            result += cards[j]
            count += 1
        if count == 3:
            check = True
            break
    if check:
        if result <= m:
            print(result)
            break
