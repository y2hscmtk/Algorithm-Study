# https://www.acmicpc.net/problem/9012

'''
괄호 검사하기
() 등과 같이 올바른 괄호라면 YES를 ()) 과 같이 틀린 괄호라면 NO를 출력한다.
'''
from collections import deque

# 테스트 케이스의 수
t = int(input())

# 괄호 계산의 원리
# 괄호 수식을 계산시 다음의 규칙대로 스택에 삽입한다
# '(' 를 만나면 스택에 넣는다.
# ')' 를 만나면 스택의 top을 팝하여 '('인지 확인하고 '(' 라면 스택에서 제거한다.
# 만약 '(' 가 아니라면 틀린 괄호가 된다.
# 위의 알고리즘을 수행한 후에 스택의 크기가 0이 아니라면 틀린 괄호가 된다.
# 위의 알고리즘을 수행한 후에 스택의 크기가 0이라면 올바른 괄호가 된다.

for i in range(t):
    # 괄호를 입력받아 저장한다.
    data = list(input())
    # 괄호를 저장할 스택 생성
    stack = deque()

    check = True
    # p = parenthesis
    for p in data:
        # 왼쪽 괄호를 만나면 스택에 삽입
        if p == '(':
            stack.append(p)
        elif p == ')':
            # 스택이 비어있지 않을때 스택의 가장 위데이터를 검사한다.
            if stack and stack[-1] == '(':
                # 가장 위의 데이터를 팝한다(제거한다.)
                stack.pop()
            else:
                # 괄호가 맞지않다면 더이상 반복하지 않고 NO출력
                print("NO")
                check = False
                break
    if check:
        # 모든 과정이 끝난 후 스택 검사
        if stack:  # 스택이 비어있지 않다면
            print("NO")
        else:
            print("YES")
