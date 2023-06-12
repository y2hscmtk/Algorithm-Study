# https://www.acmicpc.net/problem/17413
from collections import deque
# <를 만나면 flag를 활성화하고 >를 만날때까지 출력한다.
# >를 만나면 flag를 해제한다.
# 공백을 만나면 지금까지 스택에 넣어둔 단어를 차례로 팝해서 출력한다
array = list(input())
stack = [] # 스택으로 사용할 배열
queue = deque()
meet = False # <를 만났는지 확인하기 위한 플래그
for w in array: # 단어 하나씩 뽑아서 확인
    # 공백을 만나면 현재 스택에 있는 단어들 모두 출력
    if (w==' ' or w=='<') and len(stack)>0:
        while stack:
            print(stack.pop(),end='')
        if w==' ':
            print(' ',end='')
    if w=='<':
        meet=True # meet 플래그 활성화
    elif w=='>': # >만나면 비활성화
        while queue:
            print(queue.popleft(),end='')
        print(w,end='')
        meet=False
        continue
    if meet:
        queue.append(w)
    else: # 그렇지 않다면 스택에 삽입
        if w==' ':
            continue
        stack.append(w)
# 반복 이후 스택에 남아있는 것들 모두 출력
while stack:
    print(stack.pop(),end='')
