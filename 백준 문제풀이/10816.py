# https://www.acmicpc.net/problem/10816

'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
'''
n_length = int(input())
n = list(map(int, input().split()))
n.sort()  # 이진탐색을 위해 정렬
m_length = int(input())
m = list(map(int, input().split()))


# 이분 탐색을 진행하다 원하는 데이터를 찾으면 해당 인덱스를 기준으로 앞뒤로 카운팅하여 출력(같은 숫자의 경우 앞뒤에 배치되어 있을것)
# 결과 출력
for card in m:
    start, end = 0, n_length-1
    count = 0
    while start <= end:  # 다음 조건을 만족하는동안 탐색
        middle = (int)((start+end)/2)  # 중간값 파악
        if card < n[middle]:  # 탐색하고자 하는 값이 중간값보다 작다면
            end = middle - 1  # 끝점의 범위를 좁혀서 왼쪽에서 탐색
        elif card > n[middle]:  # 탐색하고자 하는 값이 중간값보다 크다면
            start = middle + 1  # 시작점의 범위를 앞으로 당겨서 오른쪽에서 탐색
        else:  # 원하는 값을 찾았을때
            # 해당 인덱스를 기준으로 앞뒤로 몇개나 있는지 판정
            count = 1
            for i in range(middle-1, -1, -1):
                if n[i] != card:
                    break
                count += 1
            for j in range(middle+1, n_length):
                if n[j] != card:
                    break
                count += 1
            print(count, end=' ')
            break
    if count != 0:
        continue
    print(0, end=' ')
