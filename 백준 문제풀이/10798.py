# https://www.acmicpc.net/problem/10798

# 최소1개에서 최대15개의 문자가 주어진다.
data = [[False]*15 for _ in range(5)]

for i in range(5):
    array = list(input())
    data[i][:len(array)] = array[:]

result = ''  # 정답 문자열
# 정답 문자열 만들기
# 세로 문자열 고정
for i in range(15):
    temp = ''
    for j in range(5):  # 가로줄
        if data[j][i] == False:
            continue
        temp += data[j][i]  # False가 아니라면 문자 저장
    result += temp

print(result)
