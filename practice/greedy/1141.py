# https://www.acmicpc.net/problem/1141
'''
알파벳 순으로 정렬 후
각 문자에 대해서 해당 문자가 다른 문자의 접두사로 포함되는지 파악
-> 접두사로 포함되는게 한개라도 존재할 경우 -1
해당 문자가 다른 모든 문자에 대해 접두사가 아니라면 접두사X 집합에 삽입

자원이 다른 자원에 포함이 될수있다는 것은 가장 크기가 작은 자원부터 비교해야 함을 의미 -> 정렬 필요
풀이참조 - x
'''
import sys
input = sys.stdin.readline

array = [] # 원본 배열
for _ in range(int(input().rstrip())):
    array.append(input().rstrip())

array.sort()

result = len(array) # 접두사 X집합의 정답 수
for i in range(len(array)):
    # 해당 문자가 다른 문자의 접두사로 포함되는지 파악
    word = array[i]
    find = False # word를 접두사로 삼는 문자가 있는지 여부
    for j in range(i+1,len(array)): # i번째 문자 이후의 다른 문자들에 대해서
        target = array[j]
        # j번째 문자가 word를 접두사로 갖는지 확인
        check = True
        for k in range(len(word)):
            if word[k] != target[k]:
                check = False
                break
        if check: # target이 word를 접두사로 갖는다면
            find = True
            break # 이후의 문자에 대해서는 확인할 필요 없음
    if find:
        result -= 1 # word를 접두사로 갖는 문자가 이후의 문자들에서 존재한다면 접두사X집합에서 제거
print(result)