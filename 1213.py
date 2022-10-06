# https://www.acmicpc.net/problem/1213

'''
임한수와 임문빈은 서로 사랑하는 사이이다.

임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.
'''

'''
아이디어
총 글자의 수가 짝수개 일때와 홀수개 일때의 상황
1. 글자수가 짝수개일때
홀수 글자의 수는 홀수 개 있어야함 짝수 글자의 수는 중요하지않음 AABBCC, AABB, AAABB,
1개만 있는 글자는 한개도 존재해서는 안됨
2. 글자수가 홀수개일때
홀수 글자의 수는 홀수 개 있어야함 AAABB AAA
1개만 있는 글자는 1개만 존재할수 있음 => 이 경우에 다른 모든 글자는 짝수개 이어야함

=> 결론적으로 짝수개의 글자는 짝이 다 맞으므로, 짝수 몇쌍이 존재하던 상관없음
홀수개의 쌍은 짝수개일때는 존재해선 안되며, 홀수개일때는 홀수개 있어야함, 1개만 있는 글자는 한개만 존재할수 있음
'''
import sys
w = input()  # 문장을 입력받음

alphabet = [w[0]]  # 글자들을 저장할 배열
alphabet_count = [1]
for i in range(1, len(w)):
    flag = True
    for j in range(0, len(alphabet)):  # 글자 배열에 저장된 단어들을과 비교
        if alphabet[j] == w[i]:  # i번째 문자와 글자배열의 해당 글자가 같다면
            alphabet_count[j] += 1
            flag = False
    if flag:
        alphabet.append(w[i])
        alphabet_count.append(1)

# 팰린드림 불가 문제에 대해서는 => I'm Sorry Hansoo 출력

count = 0
for i in range(len(alphabet_count)):
    if alphabet_count[i] == 1:
        count += 1

if count > 1:
    print("I'm Sorry Hansoo")  # 만들 수 없음
    sys.exit(0)  # 프로그램 종료
if len(w) % 2 == 0:  # 총 글자수가 짝수개 있을때
    if count >= 1:  # 1의 개수가 1개 이상 있으면 불가
        print("I'm Sorry Hansoo")  # 만들 수 없음
        sys.exit(0)  # 프로그램 종료
    else:
        for i in range(len(alphabet_count)):
            if alphabet_count[i] % 2 != 0:  # 짝수개의 글자수가 존재할경우 홀수개의 단어는 존재해서는 안됨
                print("I'm Sorry Hansoo")  # 만들 수 없음
                sys.exit(0)  # 프로그램 종료
else:
    if count == 1:  # 1의 개수가 1개일때 나머지가 모두 짝수개 이여야함
        ncount = 1
        for i in range(len(alphabet_count)):
            if alphabet_count[i] % 2 != 0:
                ncount += 1
        if ncount % 2 != 0:
            print("I'm Sorry Hansoo")  # 만들 수 없음
            sys.exit(0)  # 프로그램 종료
    else:
        # 홀수개의 단어는 홀수개만 존재할수 있음
        ncount = 0
        for i in range(len(alphabet_count)):
            if alphabet_count[i] % 2 != 0:
                ncount += 1
        if ncount % 2 == 0:  # 홀수개의 쌍이 짝수쌍 존재할경우 AAABB 불가
            print("I'm Sorry Hansoo")  # 만들 수 없음
            sys.exit(0)  # 프로그램 종료
k = 0
p = ['a']*len(w)
for i in range(len(alphabet)):
    if alphabet_count[i] % 2 != 0:  # 글자가 홀수개 일경우
        p[len(w)//2] = alphabet[i]  # 가운데에 해당 글자 삽입
    for j in range(k, alphabet_count[i]//2+k):
        p[j] = alphabet[i]
        p[len(w)-1-j] = alphabet[i]
    k += alphabet_count[i]//2

print(''.join(p))
