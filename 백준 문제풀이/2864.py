# https://www.acmicpc.net/problem/2864

a, b = list(input().split())
a_copy = a
b_copy = b

# 6을 모두 5로 바꾼값끼리 더하면, 그 값은 최솟값
a.replace('6', '5')  # 6을 5로 일괄변경
b.replace('6', '5')
min_value = int(a) + int(b)

a_copy.replace('5', '6')
b_copy.replace('5', '6')
max_value = int(a_copy)+int(b_copy)
# 5를 모두 6으로 바꾼값끼리 더하면, 그 값은 최댓값
# for i in range(len(a)):
#     if a_copy[i] == 6:
#         a_copy[i] = 5  # 5일 경우 6으로 바꾸는 연산
# for j in range(len(b)):
#     if b_copy[j] == 6:
#         b_copy[j] = 5
# max_value = int(a_copy) + int(b_copy)

print(min_value, max_value)
