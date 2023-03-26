# https://www.acmicpc.net/problem/9342
'''
상근이는 생명과학 연구소에서 염색체가 특정한 패턴인지를 확인하는 일을 하고 있다. 

염색체는 알파벳 대문자 (A, B, C, ..., Z)로만 이루어진 문자열이다. 

상근이는 각 염색체가 다음과 같은 규칙을 만족하는지 검사해야 한다.

문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
그 다음에는 A가 하나 또는 그 이상 있어야 한다.
그 다음에는 F가 하나 또는 그 이상 있어야 한다.
그 다음에는 C가 하나 또는 그 이상 있어야 한다.
그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
문자열이 주어졌을 때, 위의 규칙을 만족하는지 구하는 프로그램을 작성하시오.
'''
# 정규식을 이용한 풀이
# 정규식 정리사이트
# https://nachwon.github.io/regular-expressions/
import re
t = int(input())

'''
[abc] : abc 중 하나와 매치
A? : ? 앞에 있는 문자가 없거나 하나 있을 때 매치된다.
A+ : + 앞에 있는 문자가 최소 한 번 이상 반복되어야 매치된다.
$ : 문자열의 마지막과 매치
'''

answer = re.compile("[A-F]?A+F+C+[A-F]?$")
# [A-F]? : A-F사이의 문자가 0~1개 존재, A+F+C+ A,F,C가 각각 0~1개 존재, [A-F]? : A~F사이의 문자가 0~1개 존재 $ 문자열 종료

for _ in range(t):
    array = input()
    # 작성해둔 정규식과 문자열이 일치하지 않는다면 good, 일치한다면 Infected출력
    if answer.match(array) == None:
        print("Good")
    else:
        print("Infected!")
