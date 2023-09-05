# https://www.acmicpc.net/problem/10799
stick = input()
position = []  # 괄호의 위치를 저장하기 위함
result = 0  # 나눠진 막대의 수

for i in range(len(stick)):
    if stick[i] == '(':
        position.append(i)
    else:
        if stick[i-1] == '(':
            position.pop()
            result += len(position)
        else:
            position.pop()
            result += 1

print(result)
