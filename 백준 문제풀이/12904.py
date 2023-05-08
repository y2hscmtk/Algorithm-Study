# https://www.acmicpc.net/problem/12904

# s에서 t를 만드는 시도 => 메모리 초과 발생
# t에서 s를 만드는 과정을 역으로 생각

s = input()
t = list(input())

sucess = False # 성공여부를 저장하기 위해

def fun(array):
    global sucess
    # 성공하였다면 리턴
    if sucess:
        return
    # 두 문자열의 길이가 같아졌다면, 서로 같은 값을 갖게 되었는지 검사
    if len(array) == len(s):
        if ''.join(array) == s:
            sucess = True # 성공처리
        return # 두 문자열이 같아졌다면 성공여부와 관계없이 리턴
    # 두 문자열의 길이가 아직 같지 않다면 t를 s로 만드는 과정 역산
    # 규칙 1 : 문자열 뒤에 A를 추가한다.
    # 규칙 2 : 문자열을 뒤집고 뒤에 B를 추가한다.
    # => 가장 뒤의 문자가 어떤 문자인지 확인하여 판단
    alpha = array.pop() # 가장 뒷 문자 팝
    if alpha == 'A': # A이면 문자열 제거한 상태로 fun수행
        fun(array)
    else: # 'B'인 경우
        fun(array[::-1]) # 문자열 뒤집은 후 fun 수행

fun(t)
print(1) if sucess else print(0)
