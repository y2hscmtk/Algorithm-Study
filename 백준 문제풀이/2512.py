# https://www.acmicpc.net/problem/2512

'''
먼저 입력받은 예산요청을 정렬한뒤, 이분 탐색을 통해 상한액을 설정한다.
low를 가장 작은 예산요청값으로 설정하고, 전체 국가예산액을 high로 설정한다.
설정된 상한액을 함수로 보내어 가능한 한 최대한의 총 예산을 업데이트한다.
최대예산의 값이 더 높게 변경된다면 상한액을 정하기 위한 이분탐색을 더 수행하지 않는다.
'''

n = int(input())
data = list(map(int, input().split()))

data.sort()  # 오름차순 정렬 => 이분탐색을 위해
# 전체 국가예산액
max_money = int(input())


result = 0  # 최대 총 예산
last = 0  # 이전에 계산된 총 최대 예산

high = max_money
low = 0


# 이분탐색 시행
def update(money):
    global last, result
    temp = 0  # 총 예산을 누적시켜 저장
    # 총 예산 계산
    for i in range(len(data)):
        # 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정
        if data[i] <= money:
            temp += data[i]
        else:
            temp += money  # 상한액 초과금에 대해서는 상한액만 배정
    # 전체 국가 예산액을 넘지 않는지 확인
    if temp <= max_money:
        # 국가 예산액을 넘기지 않는다면
        # 기존 최대 예산액(last)보다 더 커지는지 확인한다.
        if last <= temp:
            last = temp  # 최대 예산액 업데이트
            result = mid  # 현재 금액이 상한액일때(mid) 최대 예산액을 얻을수 있으므로 업데이트
            return True  # 상한액이 업데이트 되었다면 True리턴

    # 전체 국가 예산액을 넘긴다는것은
    # 기존 수들을 다 더한값이 전체 국가 예산액보다 많을경우를 의미
    # => 상한액을 줄여야함(기존값들이 다 들어갔다는것이므로)
    # => 상한액을 줄이기 위해서는 high의 범위를 mid로 줄여야함
    return False  # => false => high = mid


# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
if sum(data)<=max_money:
    print(data[-1]) # 배정된 예산들 중 최대값인 정수를 출력한다.
else:
    # 반복문 불변조건
    while low < high:
        # 중간값 설정
        mid = (low+high)//2
        # 중간값을 함수로 넘겨서 최대 총 예산이 더 커지는지 확인
        if update(mid):  # 더 커졌다면
            low = mid+1  # high보다 작고 mid보다 큰 값들중에 조건을 만족하는 값이 있는지 탐색
        else:
            high = mid

    print(result)
