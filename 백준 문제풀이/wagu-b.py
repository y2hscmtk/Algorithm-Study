# 만들수있는 숫자들 표시
point = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# # 모두 2개씩 가져갈수 있다는 의미에서
# count = [2 for i in range(len(point))]

a, b = map(int, input().split())

number = []


def check_point(check, data):
    while True:
        if data >= check:
            number.append(check)
            data -= check
        check //= 2
        if data == 0:
            return


# a,b에서 숫자들 각각 계산하기
check_point(512, a)
check_point(512, b)

result = 0

for n in point:
    if number.count(n) == 1:
        result += n

print(result)
