# 백준 2437번

# https://www.acmicpc.net/problem/2847

# 아이디어 : 결국 단계별로 점수가 올라가도록 만들면 되기 때문에, 마지막 레벨의 점수에서 1씩 감소한 점수를 받도록 만들면 된다.

# n = int(input())  # 레벨의 개수 입력받기

# point = []

# for i in range(n):
#     point.append(int(input()))  # 레벨별로 얻을 점수를 입력받는다

# max_point = point[n-1]  # 최종레벨의 점수를 최대 점수로 설정한뒤

# hope_point = [0]*n  # 점수가 1씩 줄어드는 이상적인 점수 배열을 생성한다.
# for i in range(n-1, -1, -1):
#     hope_point[i] = max_point
#     max_point -= 1  # 값을 1씩 줄여가며 희망 점수배열에 삽입한다.

# result = 0  # 원하는 배열을 만들기 위한 최소 횟수를 저장할 변수

# for i in range(n):
#     result += (point[i]-hope_point[i])  # 이상적인 배열을 만들기 위한 감소 횟수를 저장한다.

# print(result)

# 아이디어2 : 마지막 레벨이 몇점이나 높던지는 상관없이, 다음단계를 레벨이 이전단계레벨보다 점수가 높으면 된다.
n = int(input())

point = []

for i in range(n):
    point.append(int(input()))  # 레벨별로 얻을 점수를 입력받는다

result = 0
for i in range(n-1, 0, -1):
    if point[i] <= point[i-1]:  # 현재 레벨의 점수가 이전단계를 레벨의 점수보다 작거나 같아면
        result += (point[i-1]-(point[i]-1))
        point[i-1] = point[i]-1

print(result)
