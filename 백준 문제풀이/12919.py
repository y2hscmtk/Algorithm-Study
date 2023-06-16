# https://www.acmicpc.net/problem/12919
'''
두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 

문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.

1. 문자열의 뒤에 A를 추가한다.
2. 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 

S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.
'''
s = input()
t = list(input())

success = False

# s에서 t로 바꾸지말고, t에서 s로 바꾸는 연산을 수행한다
# 1. 문자열 뒤에 A를 제거한다
# 2. 문자열을 뒤집고, B를 제거한다.

# 글자수가 같아질때까지 1,2 연산을 수행한다
# 글자수가 같음에도 불구하고 원하는 수를 만들지 못했다면 실패 => 재귀에서 탈출한다.

def check(array):
    global success
    # 이미 성공했다면 재귀를 수행할 필요가 없으므로, 성공 여부 확인
    if success:
        return # 성공했다면 다른 재귀 수행 없이 종료
    
    if len(array)==len(s): # s와 길이가 똑같아졌다면
        # 같은 글자인지 확인
        if ''.join(array)==s: # 같은 글자라면
            success = True # 성공처리
        # 성공유무와 무관하게 재귀 종료
        return
    # 길이가 같지 않다면 재귀 수행
    # 1,2번 연산 수행
    # 문자열의 뒤에 A가 있다면 A제거 연산 수행
    if array[-1] == 'A':
        check(array[:-1])
    # B를 제거하고 문자열을 뒤집는다.
    # 문자열의 맨 앞이 B라면 2번 연산 수행
    if array[0] == 'B':
        array = array[1:] 
        check(array[::-1])
    
check(t)
# 성공했다면 1, 실패했다면 0 출력
print(1) if success else print(0)