# https://www.acmicpc.net/problem/2607
'''
두 단어가 같은 구성을 갖거나
한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우
두가지 경우에 해당하면 비슷한 단어라고 한다

첫번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하라
'''
import copy
n = int(input())

word = [input() for _ in range(n)]

# 첫번째 단어의 구성 파악
original = {}

for alphabet in word[0]:
    # 이미 키가 존재한다면, 개수를 증가시킨다.
    if alphabet in original:
        original[alphabet] += 1
    # 처음 발견한 단어라면 1개로 기록한다.
    else:
        original[alphabet] = 1

# 정답 출력용
result = 0

# 비슷한 단어 탐색
for i in range(1, n):
    # 첫번째 단어에 대한 딕셔너리 깊은 복사
    first = copy.deepcopy(original)

    # 확인할 단어의 구성을 저장할 딕셔너리
    check = {}
    # i번째 단어의 구성 파악
    for alphabet in word[i]:
        # 이미 키가 존재한다면, 개수를 증가시킨다.
        if alphabet in check:
            check[alphabet] += 1
        # 처음 발견한 단어라면 1개로 기록한다.
        else:
            check[alphabet] = 1

    # 구성이 같지 않을경우, 차이가 몇개나는지확인
    count = 0
    error = False
    # 파악한 단어와 첫번째 단어가 같은 구성인지 확인
    for alphabet in check:
        # 먼저 첫번째단어 딕셔너리에 해당하는 단어가 존재하는지 확인
        if alphabet in first:
            # 개수가 같은지 확인
            if first[alphabet] != check[alphabet]:
                count += abs(check[alphabet]-first[alphabet])
                # 해당하는 단어의 값은 이미 비교가 끝났으므로 first에서 제거
            del first[alphabet]
        # 해당하는 단어가 없다면
        else:
            count += check[alphabet]  # 알파벳 개수만큼 카운트
        # 차이가 2이상 난다면
        if count > 1:
            error = True
            break  # 비슷한 단어가 될 수 없음
    # 비교이후 first에 남아있는 단어의 개수만큼 count증가
    if len(first) != 0:
        for alphabet in first:
            count += first[alphabet]
            if count > 1:
                error = True
                break
    # 에러가 없었다면 result 증가
    if not error:
        result += 1

print(result)
