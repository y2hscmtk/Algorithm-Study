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

=> 9퍼센트에서 실패
'''


'''
새로운 아이디어

아몰라 그냥 배치하고 펠린드롬검사해서 실패하면 아임쏘리 출력할래
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

# 아몰라 그냥 일단 배치해
pl = ['A']*len(w)
k = 0
check = True
for i in range(len(alphabet)):
    if (check):
        if alphabet_count[i] % 2 != 0:
            pl[len(w)//2] = alphabet[i]
            check = False
    else:
        print("I'm Sorry Hansoo")  # 거 미안하게 됐수다
        sys.exit(0)
    for j in range(k, alphabet_count[i]//2+k):
        pl[j] = alphabet[i]
        pl[len(w)-1-j] = alphabet[i]
    k += (alphabet_count[i]//2)

# 팰린 뭐시기 그거 검사 실시
for i in range(len(pl)//2):
    if pl[i] != pl[len(pl)-1-i]:  # 두 단어가 일치하지 않는 경우
        print("I'm Sorry Hansoo")  # 거 미안하게 됐수다
        sys.exit(0)

print(''.join(pl))  # 완성된 단어
