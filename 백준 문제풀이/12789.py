# https://www.acmicpc.net/problem/12789
'''
스택 활용
순서를 기록하기 위한 변수 -> 1부터 시작
가장 첫번째 사람의 수부터 탐색, 순서변수와 동일한 숫자면 다음 숫자로 이동
그렇지 않다면
1. 스택이 비어있다 -> 스택에 삽입
2. 스택이 비어있지 않다 -> 팝해서 변수와 동일한지 확인, 동일하지 않다면 순서가 꼬인것 Sad
끝까지 모두 돌렸다 -> Nice
'''
import sys
input = sys.stdin.readline
input();people = list(map(int,input().split()))
i,next = 0,1 #사람 배열 인덱스, 다음사람의 번호
stack = []
while i!=len(people):
    if people[i] == next: # 다음 사람의 번호가 다음 번호와 동일하다면
        next+=1;i+=1
    else:
        if len(stack)!=0: # 스택이 비어있는지 확인
            snum = stack[-1]
            if snum == next: # 맞는지 확인하고 비우기
                next+=1
                stack.pop()
            else: # 번호가 다르다 -> 스택에 넣기
                stack.append(people[i])
                i+=1
        else: # 다음 사람번호와 동일하지 않고 스택이 비어있다면
            stack.append(people[i]) # 사람 삽입
            i+=1
# 스택에 남이있는 사람들에 대해서
success = True
while stack:
    if next != stack.pop():
        success = False
    next+=1

print("Nice" if success else "Sad")