# https://www.acmicpc.net/problem/25501
'''
재귀함수를 이용하여 팰린드롬 여부 출력
팰린드롬이면 1 아니면 0
판별 과정중에 재귀함수가 몇번 호출되었는지도 함께 출력
'''
def recursion(s, l, r):
    global count
    count += 1 # 재귀 호출된 시점에서 count +=1
    if l >= r: return 1 # 모든 문자를 다 확인한 경우
    elif s[l] != s[r]: return 0 # 하나라도 다른 문자가 발견된 경우
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count = 0 # 재귀 횟수 카운트용 전역변수 초기화
    return recursion(s, 0, len(s)-1)

count = 0
for _ in range(int(input())):
    S = input() # 팰린드롬을 판별할 문자열
    print(isPalindrome(S),count)
    