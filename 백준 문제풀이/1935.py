# https://www.acmicpc.net/problem/1935
'''
[후위 표기식]
숫자를 만나면 푸쉬
연산자를 만나면 숫자 2개 팝한후 연산 수행하여 다시 푸쉬
계산 결과를 소숫점 둘째 자리까지 출력한다.
'''
import sys
input = sys.stdin.readline
operator = "*/+-"
n = int(input())
query = input().rstrip()
data = []
# 계산에 사용할 숫자들 입력받기

for i in range(n):
    data.append(input().rstrip())
# 쿼리를 보고 스택에 데이터 삽입
stack = []
for i in query:
    if i not in operator:  # 연산자가 아닌 숫자(알파벳)라면
        stack.append(data[ord(i)-ord('A')])  # 해당 숫자 스택에 삽입
    else:  # 연산자라면
        # 두 숫자 차례로 꺼내고
        n2 = stack.pop()
        n1 = stack.pop()
        new_data = eval(n1+i+n2)  # 연산 수행
        stack.append(str(new_data))  # 새로운 숫자 삽입

result = float(stack[0])
print("%0.2f" % result)
# print("{:.2f}".format(result)) 소수점 2자리까지 표현하는 다양한 방법
# print(f'{result:.2f}')
