# https://www.acmicpc.net/problem/3135
a, b = map(int, input().split())
save = []
for _ in range(int(input())):
    save.append(int(input()))
count = 0  # 버튼을 누르는 횟수
save.sort()

# 그리디
temp = -1
for i in range(len(save)):
    if save[i] == b:
        temp = save[i]
        count += 1
        break
    elif save[i] > b:
        # b보다 작은수와 큰 수 중에 더 근접한 것으로 temp지정
        temp = save[i] if abs(b-save[i]) < abs(b-save[i-1]) else save[i-1]
        count += 1  # temp번호로 이동하기 위해 버튼을 누름
        break
# 수를 모두 돌았음에도 temp가 여전히 -1이다 => 목적지 번호보다 모두 낮다
if temp == -1:
    temp = save[-1]  # 가장 큰수로 설정
    count += 1
# temp를 구했으면 b에서 temp를 뺀만큼 수동으로 주파수를 조절해야함
# 저장되어 있는 버튼을 이용하지 않는게 나을때도 존재함 => 마지막에 비교
count = min(count+abs(b-temp), abs(a-b))
print(count)
