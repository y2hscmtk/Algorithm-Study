# https://www.acmicpc.net/problem/4949
'''
왼쪽 괄호를 만나면 스택에 push한다
오른쪽 괄호를 만나면(종류 무관) 스택에서 pop하여 같은 종류인지 확인한다.
만약 같은 종류의 괄호라면 제거하고, 그렇지 않다면 잘못된 문장이다.
탐색이 끝난 이후, 스택에 데이터가 남아있다면(왼쪽 괄호가 닫히지 않은 경우에 해당)
잘못된 문장임을 의미한다.
'''
# 온점이 입력될때까지 반복한다.
import sys
input = sys.stdin.readline
while True:
    data = input().rstrip()
    # 마지막 입력은 오직 온점 하나로 끝난다.
    if data=='.':
        break
    stack = []
    error = False
    for a in data:
        if a =='(' or a=='[':
            stack.append(a)
        # 닫힌 괄호를 발견하면 확인      
        elif a==')' or a==']':
            # 먼저 스택에 값이 없다면 오류
            if len(stack) == 0:
                error = True
                break
            top = stack.pop()
            # 괄호가 올바르다면 넘어감
            if top == '(':
                if a!=')':
                    error = True
                    break
            elif top=='[':
                if a!=']':
                    error = True
                    break
    # 비교가 끝난뒤 스택에 데이터가 남아있다면 
    if len(stack)>0 or error:
        print("no") # 올바르지 않은 문장임
    else:
        print("yes")
