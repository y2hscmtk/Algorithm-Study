from itertools import combinations

n, m = map(int, input().split())
# 카드 데이터 입력받기
card = list(map(int, input().split()))
# m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합을 출력한다.
result = -1  # 정답을 저장할 변수

# m에 최대한 가까운 카드 3장의 합, 경우의 수 모두 따져보기
for x, y, z in combinations(card, 3):
    card_sum = x+y+z  # 조합에서 생성된 카드의 합 계산
    if card_sum > m:  # 카드의 합이 더 크다면 무시
        continue
    else:
        result = max(result, card_sum)  # 더 큰 값으로 갱신

print(result)
