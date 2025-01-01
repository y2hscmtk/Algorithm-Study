# # HashMap / 두 수의 합
'''
n개의 정수가 입력으로 주어지고, 이 중 서로 다른 위치에 있는 두 개의 수를 뽑아 더했을 때 k가 되는 가짓수를 구하는 프로그램을 작성해보세요.

풀이참조
'''
n,k = map(int,input().split())
count = dict()
data = list(map(int,input().split()))

ans = 0
# 뒤에서부터 앞으로 이동하며 이미 기록된 수만 카운트하므로, 중복 카운팅 걱정이 없음
for elem in data:
    target = k - elem # 목표 수

    # 조건을 만족하는 순서쌍이 존재한다면
    if target in count:
        ans += count[target]

    # 현재 숫자 빈도수 기록
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

print(ans)