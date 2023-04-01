# https://www.acmicpc.net/problem/2670
'''
문제
N개의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아, 그 곱을 출력하는 프로그램을 작성하시오. 
예를 들어 아래와 같이 8개의 양의 실수가 주어진다면,
1.1/0.7/[1.3/0.9/1.4]/0.8/0.7/1.4
색칠된 부분의 곱이 최대가 되며, 그 값은 1.638이다.
'''
n = int(input())

# 실수 입력받기
number = []
for i in range(n):
    number.append(float(input()))


result = -1  # 최대값을 저장하기 위해


# 구간을 달리하면서 dp에 값을 저장하고
# 쵀대값을 갱신해주면 될듯

# 시작 구간
for i in range(n):
    # # dp 테이블 생성 해당 인덱스 구간까지의 최대곱을 갱신하기 위한 공간
    # dp = [0 for _ in range(i)]
    temp = number[i]
    for j in range(i+1, n):
        # 수를 곱함으로써 더 수가 커진다면
        if result < temp*number[j]:
            result = max(temp, temp*number[j])
            temp *= number[j]
            # temp = temp*number[j]  # temp값 갱신
        else:
            break  # 더이상 수를 곱해나가지 않음
    result = max(result, temp)  # 정답 갱신

result = round(result, 3)
print(result)
