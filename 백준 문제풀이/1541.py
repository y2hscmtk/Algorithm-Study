# https://www.acmicpc.net/problem/1541
'''
식의 값을 최소로 만들기 위한 방법
=> -의 뒤에 결과를 괄호로 묶으면 됨
a + b - c + d - e
=> (a+b)-(c+d)-e
=> -를 기준으로 서로 묶어서 계산을 할 때가 가장 최소가 된다.
=> '경계'를 잘 설정하는 것
'''
data = input().split('-') # -를 기준으로 식을 나눈다.

new = []
# 괄호 안의 내용은 다시 +를 기준으로 나누기
for i in range(len(data)):
    data[i] = data[i].split('+')
    new.append(0)
    for num in data[i]:
        new[i] += int(num)
# 만들어진 내용들 서로 빼기
result = 2*new[0]
for i in range(len(new)):
    result -= new[i]

print(result)