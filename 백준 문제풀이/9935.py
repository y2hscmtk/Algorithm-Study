# https://www.acmicpc.net/problem/9935

'''
상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
'''
'''
반복문을 이용하여 문자열의 모든 문자를 하나씩 검사하여, 찾고자하는 문자열의 첫번째 문자가 일치하면
해당 문자를 기준으로 다시 찾고자 하는 문자열과 일치하는지 검사하여 del 명령으로 일치하는 문자를 지운후 다음 문자부터 반복한다.
반복이 종료된 이후, 문자열의 길이를 확인하여 남아있는 문자가 없다면 FRULA를 출력하고. 남아있는 문자가 있다면 해당 문자를 출력한다
'''
# 원본 문자열
words = list(input())
# 폭발시킬 문자열
search = list(input())

i = 0
while i != len(words):
    index = 0
    flag = True
    if words[i] == search[index]:
        index += 1
        s = i  # 시작 인덱스
        correct = True
        for j in range(i+1, i+len(search)):
            if words[j] == search[index]:
                index += 1
            else:
                correct = False
                break
        if correct:  # 문자열이 일치한다면
            del words[s:j+1]
            i = 0  # 다시 첫번째 인덱스로 변환
            flag = False  # i값 중복변환 방지
    if flag:
        i += 1  # 다음 인덱스로

if len(words) != 0:
    for word in words:
        print(word, end='')
else:
    print("FRULA")
