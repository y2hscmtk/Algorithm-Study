# https://www.acmicpc.net/problem/2961
'''
도영이는 짜파구리 요리사로 명성을 날렸었다. 이번에는 이전에 없었던 새로운 요리에 도전을 해보려고 한다.

지금 도영이의 앞에는 재료가 N개 있다. 도영이는 각 재료의 신맛 S와 쓴맛 B를 알고 있다. 

여러 재료를 이용해서 요리할 때, 그 음식의 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.

시거나 쓴 음식을 좋아하는 사람은 많지 않다. 도영이는 재료를 적절히 섞어서 요리의 신맛과 쓴맛의 차이를 작게 만들려고 한다. 

또, 물을 요리라고 할 수는 없기 때문에, 재료는 적어도 하나 사용해야 한다.

재료의 신맛과 쓴맛이 주어졌을 때, 신맛과 쓴맛의 차이가 가장 작은 요리를 만드는 프로그램을 작성하시오.
'''
'''
재료를 1개부터 N개 선택하는 모든 경우의 수에 대해서,각각 신맛과 쓴맛을 구하고
신맛과 쓴맛의 차를 기존의 최소값과 비교하여 업데이트
'''
import sys
from itertools import combinations
n = int(input())
# 재료 정보 (신맛, 쓴맛) 입력받기
food = [list(map(int, input().split())) for _ in range(n)]

result = sys.maxsize  # 신맛과 쓴맛의 최소값

# 재료를 1개부터 n개 선택하는 모든 경우의 수
for i in range(1, n+1):
    # 재료를 i개 선택하는 모든 경우 => selected_food
    for selected_food in combinations(food, i):
        # 신맛, 쓴맛 초기화
        sour, written = 1, 0
        # 선택된 재료들을 대상으로 신맛 쓴맛 계산
        for s, b in selected_food:
            sour *= s  # 신맛은 재료들의 곱
            written += b  # 쓴맛은 재료들의 합
        # 최종적으로 쓴맛과 신맛의 차가 가장 적게 되어야함
        # 기존 최소값과 비교하여 작은값 업데이트
        result = min(abs(sour-written), result)

# 모든 경우의 수를 돌려봤을 때
# 쓴맛과 신맛의 최소값 출력
print(result)
