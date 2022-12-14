# https://www.acmicpc.net/problem/10773

# 수를 입력받아 합을 구한다. 0을 입력할경우 최근에 입력받은 수를 지운다. 마지막에 최종합을 출력한다.

# 스택 자료구조를 이용한다.

k = int(input())

data = []  # 수를 저장할 스택


for i in range(k):
    number = int(input())  # 수를 하나 입력받는다.
    if number == 0 and len(data) != 0:  # 스택이 비어있지 않다면(즉 삭제할 수가 존재한다면)
        data.pop()  # 가장 최근 입력받은 수를 제거한다.
    else:  # 0이 아닌 수를 입력했다면
        data.append(number)  # 스택에 값을 저장한다.

# 모든 수의 합을 출력한다.
print(sum(data))
